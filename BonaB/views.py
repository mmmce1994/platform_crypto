# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from BonaB.models import *
from rest_framework import viewsets
from BonaB.serializers import *
from rest_framework import permissions
from BonaB.permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from subprocess import PIPE, Popen
import subprocess, shutil, os
from github import Github
import threading
from django.template import RequestContext
from multiprocessing import Process
import hashlib
import constants
import random
import pyping
import sys

reload(sys)
sys.setdefaultencoding('utf8')



# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:

        username = request.POST.get('signin-username', '')
        pwd = request.POST.get('signin-pwd', '')
        user = authenticate(username=username, password=pwd)

        if user is not None:
            auth_login(request, user)
            return render(request, "../templates/admin/index.html")
        else:
            return render(request, "../templates/admin/login.html")


def list_cc(request):
    if request.user.is_authenticated:
        ccList = CryptoCurrency.objects.filter(owner=request.user)
        return render_to_response("../templates/admin/list-cc.html", {"ccList": ccList})
    else:
        return HttpResponseRedirect('/')


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:

        return render_to_response("../templates/admin/index.html", {"genesis": get_server_ping()})

def get_server_ping() :

    hostname = "192.168.1.7"  # example
    response = subprocess.call("ping -c 1 %s" %hostname, shell=True)
    return not response


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def ccDetails(request, currency_id):
    if request.user.is_authenticated:
        cc = CryptoCurrency.objects.get(id=currency_id)
        fnList = FullNode.objects.filter(cryptoCurrency=cc)
        platformList = Platform.objects.filter(cryptoCurrency=cc)
        return render_to_response("../templates/admin/ccDetails.html", {"cc": cc, "fnList": fnList, "platforms":platformList})

    else:
        return HttpResponseRedirect("/")


def ansibleGenesisRunner(currency_id):
    subprocess.call("python genesisminerrunner.py %s" %currency_id, shell=True, cwd="./ansibleserver/")

def ansibleCoreBuilder(gitUrl, currency_id, platform):
    subprocess.call("python corebuilderrunner.py %s %s %s" %(gitUrl, currency_id, platform), shell=True, cwd="./ansibleserver/")

def asnibleApacheServer(username, password, filename, platform):
    subprocess.call("python apacheserverrunner.py %s %s %s %s" %(username, password, filename, platform), shell=True, cwd="./ansibleserver/")

def ansibleAndroidBuilder(gitUrl, currency_id):
    subprocess.call("python androidbuilderrunner.py %s %s" % (gitUrl, currency_id), shell=True, cwd="./ansibleserver/")


def newCC(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            data = dict(request.POST)
            print data

            cc = CryptoCurrency(
                                currencyName=data['currencyName'][0],
                                pszTimestamp=data['pszTimestamp'][0],
                                maxMoney=data['maxMoney'][0],
                                halvingInterval=data['halvingInterval'][0],
                                nDefaultPort=data['nDefaultPort'][0],
                                nTime=data['nTime'][0],
                                nBits=data['nBits'][0],
                                nSubsidy=data['nSubsidy'][0],
                                coinBase=data['coinBase'][0],
                                pubKey=data['pubKey'][0],
                                githubUser=data['githubUser'][0],
                                githubPass=data['githubPass'][0],
                                currencyUnit=data['currencyUnit'][0],
                                description=constants.PROCESSING_GENESIS_BLOCK,
                                status=constants.COIN_STATUS_PROCESSING,
                                owner=request.user,
                                downloadPassword=makePassword()
                                )



            cc.hashGenesisParams = make_hash([cc.nBits, cc.pszTimestamp, cc.pubKey, cc.nTime, cc.coinBase])




            errors = []

            try:
                g = Github(data['githubUser'][0], data['githubPass'][0]).get_user()
                g.get_emails()[0]
            except:

                error = "github cannot login!"
                errors.append(error)
                pass
            if CryptoCurrency.objects.filter(hashGenesisParams=cc.hashGenesisParams).count() :
                error = "genesis will not be unique!"
                errors.append(error)


            #if  get_bcaddress_version(cc.pubKey) is None :
                #error = "invalid pubKey!"
                #errors.append(error)

            if len(errors) :
                return render(request, "../templates/admin/newCC.html", {"errors": errors})

            cc.save()

            Platform(name="windows", aliasName="core", haveBuild=True, cryptoCurrency=cc).save()
            Platform(name="linux", aliasName="core", haveBuild=True, cryptoCurrency=cc).save()
            Platform(name="bitcore", aliasName="core+", haveBuild=True,cryptoCurrency=cc).save()
            Platform(name="android", aliasName="android", haveBuild=True, cryptoCurrency=cc).save()
            Platform(name="seeder", cryptoCurrency=cc).save()
            #Platform(name="ios", cryptoCurrency=cc).save()

            for key,value in data.items():
                if key.startswith("domain") :
                    subDomain = data["subDomain"+key[6:]][0]
                    print subDomain
                    DnsSeed(domain=value[0], subDomain=subDomain, cryptoCurrency=cc).save()

                elif key.startswith("address") :
                    FullNode(address=value[0], cryptoCurrency=cc).save()




            f = open("./ansibleserver/jsonfiles/%s.json" % cc.id, "w")
            f.write('{"id": %s, "nbits":"%s", "psztimestamp":"%s", "pubkey":"%s", "ntime":"%s", "coinbase":"%s" }' % (
            cc.id, cc.nBits[2:], cc.pszTimestamp, cc.pubKey, format(int(cc.nTime),'x'), int(cc.coinBase) * (100000000)))
            f.close()

            t = threading.Thread(target=ansibleGenesisRunner, args=[cc.id])
            t.daemon = True
            t.start()





            return HttpResponseRedirect('/dashboard/list')

        else:
            return render(request, "../templates/admin/newCC.html")


    else:
        return HttpResponseRedirect('/')


def ccDelete(request, currency_id):
    currency = CryptoCurrency.objects.get(id=currency_id)

    # delete all full nodes of currency
    fullNodeList = FullNode.objects.filter(cryptoCurrency=currency)
    for fn in fullNodeList:
        fn.delete()

    # delete genesis of currency and itself
    try:
        GenesisBlock.objects.get(cryptoCurrency=currency).delete()
    except:
        print "there is no genesis block for %s" % currency.currencyName

    currency.delete()

    return HttpResponseRedirect('/dashboard/list')


def build_core(currency, platform) :

    gitUrl = "https://github.com/%s/%s-%s.git" %(currency.githubUser, platform.name,  currency.currencyName)
    t = threading.Thread(target=ansibleCoreBuilder, args=[gitUrl, currency.id, platform])
    t.daemon = True
    t.start()


def platform_build(request, currency_id,platform_id):

    platform = Platform.objects.get(id = platform_id)
    currency = CryptoCurrency.objects.get(id = currency_id)

    platform.buildStatus = 1
    platform.save()

    if platform.aliasName == "core":

        t = threading.Thread(target=ansibleCoreBuilder, args=[platform.githubUrl, currency.id, platform.name])

    else:

        t = threading.Thread(target=ansibleAndroidBuilder, args=[platform.githubUrl, currency.id])

    t.daemon = True
    t.start()
    return HttpResponseRedirect('/dashboard/list/%s' %platform.cryptoCurrency.id)



def push_on_github(currency):

    pubkeyName = "id_rsa_%s.pub" % currency.githubUser
    keyName = "id_rsa_%s" % currency.githubUser
    keyAddress = os.getcwd()+"/BonaB/keys/"
    githubUser = currency.githubUser
    githubPass = currency.githubPass
    print "Start git ..."
    error = 0

    #android platform will be add ...
    windows_platform = Platform.objects.get(name="windows", cryptoCurrency=currency)
    linux_platform = Platform.objects.get(name="linux", cryptoCurrency=currency)
    bitcore_platform = Platform.objects.get(name="bitcore", CryptoCurrency=currency)
    android_platform = Platform.objects.get(name="android", cryptoCurrency=currency)
    seeder_platfrom = Platform.objects.get(name="seeder", cryptoCurrency=currency)
    platforms = [linux_platform, bitcore_platform, seeder_platfrom, android_platform]


    try :

        #step 1 : prepare github

        key = create_sshKey(keyName, pubkeyName, keyAddress, githubUser)
        g = Github(githubUser, githubPass)
        gituser = g.get_user()
        gituser.create_key("server", key)
        githubEmail = gituser.get_emails()[0]["email"]

        #create repositories
        for platform in platforms :
            gituser.create_repo(platform.name + "-" + currency.currencyName)


    except :
        error = 1

    finally:

        if error :
            currency.status = constants.COIN_STATUS_FAIL
            currency.description = constants.FAILED_GITHUB_PREPARE
            currency.save()

        else:

            currency.description = constants.PROCESSING_GIT_PUSH
            currency.save()

            currencyName = currency.currencyName
            results = []


            for platform in platforms :
                new_path = "./sources/new%s-%s" % (platform.aliasName, currency.id)
                repoName = "%s(%s)-%s" %(platform.name, platform.aliasName, currencyName)
                platform.repoStatus = 1
                platform.save()

                if platform.name == "linux":
                    windows_platform.repoStatus = platform.repoStatus
                    windows_platform.save()

                result = push_github(new_path, githubUser, githubEmail, repoName)

                if result == 0 :
                    platform.repoStatus = 2
                    sha = str(gituser.get_repo(repoName).get_commits()[0].sha)
                    platform.hashCommit = sha
                    platform.githubUrl = make_githubUrl(githubUser, platform.name, currencyName)
                    platform.save()

                    if platform.name == "linux":
                        windows_platform.repoStatus = platform.repoStatus
                        windows_platform.hashCommit = platform.hashCommit
                        windows_platform.githubUrl = platform.githubUrl
                        windows_platform.save()



                else:
                    platform.repoStatus = 3
                    platform.save()

                    if platform.name == "linux":
                        windows_platform.repoStatus = platform.repoStatus
                        windows_platform.save()



            # remove all temp keys
            os.remove(keyAddress + keyName)
            os.remove(keyAddress + pubkeyName)

            currency.status = constants.COIN_STATUS_SUCCESS
            currency.description = ""
            currency.save()





def make_githubUrl(githubUser, platformName, currencyName):
    baseUrl = "https://github.com/%s/%s-%s"
    githubUrl = baseUrl %(githubUser, platformName, currencyName)
    return githubUrl


def create_sshKey(keyName, pubkeyName, keyAddress, githubUser):

    key = None

    try :
        subprocess.call('ssh-add -D', shell=True)
        p = Popen(["ssh-keygen", "-t", "rsa", "-b", "4096", "-C", "test@gmail.com"], stdout=PIPE, stdin=PIPE,
                  cwd=keyAddress)
        p.communicate(keyName)
        subprocess.call("ssh-add %s" % keyAddress + keyName, shell=True)
        key = open(keyAddress + pubkeyName).read()

        config = open("/home/mahdi/.ssh/config", "a")
        config.write("Host %s.github.com\n" % githubUser)
        config.write("      HostName github.com\n")
        config.write("      PreferredAuthentications publickey\n")
        config.write("      IdentityFile %s" % keyAddress + keyName)
        config.write("\n\n\n")
        config.close()

    except :
        pass

    return key




def push_github(new_path, githubUser, githubEmail, repoName):

    outputs = []
    result = 0

    outputs.append(subprocess.call("git init", shell=True, cwd=new_path))
    outputs.append(subprocess.call("git config user.name " + githubUser, shell=True, cwd=new_path))
    outputs.append(subprocess.call("git config user.email " + githubEmail, shell=True, cwd=new_path))
    outputs.append(subprocess.call("git add .", shell=True, cwd=new_path))
    outputs.append(subprocess.call("git commit -m 'init'", shell=True, cwd=new_path))
    outputs.append(subprocess.call("git remote add origin git@%s.github.com:%s/%s.git" % (
    githubUser, githubUser, repoName), shell=True, cwd=new_path))
    outputs.append(subprocess.call("git push -u origin master", shell=True, cwd=new_path))

    shutil.rmtree(new_path)

    for output in outputs:
        result += output

    return result




def edit_seeder_code(currency_id, changesDict):

    print "start editing seeder ..."

    source_code_path = "./sources/seeder"
    new_source_path = "./sources/newseeder-%s" %currency_id
    shutil.copytree(source_code_path, new_source_path)
    print "copied tree!"
    for dirpath, dirname, filename in os.walk(new_source_path):  # Getting a list of the full paths of files

        for fname in filename:
            path = os.path.join(dirpath, fname)  # Joining dirpath and filenames
            f = open(path)
            strg = f.read() # Opening the files for reading only
            f.close()
            for oldStr, newStr in changesDict.items():
                try:
                    strg = strg.replace(oldStr, newStr)
                except Exception:

                    print "exception at editing seeder"
                    pass

            f = open(path, 'w')  # We open the files with the WRITE option
            f.write(strg)  # We are writing the the changes to the files
            f.close()  # Closing the files

    print "seeder edited!"




def edit_core_code(currency_id, type, changesDict):


    def rename(path, oldstr, newstr):
        for files in os.listdir(path):
            os.rename(os.path.join(path, files), os.path.join(path, files.replace(oldstr, newstr)))



    print "start editing %s ..." %type

    source_code_path = "./sources/%s/utabit" %type
    new_source_path = "./sources/new%s-%s" %(type, currency_id)
    shutil.copytree(source_code_path, new_source_path)
    print "copied tree!"
    for dirpath, dirname, filename in os.walk(new_source_path):  # Getting a list of the full paths of files

        for fname in filename:
            path = os.path.join(dirpath, fname)  # Joining dirpath and filenames
            f = open(path)
            strg = f.read() # Opening the files for reading only
            f.close()
            for oldStr, newStr in changesDict.items():
                try:
                    strg = strg.replace(oldStr, newStr)
                except Exception:
                    print type(strg)
                    pass
                    #print("failed at edit core")
                    #print(type(oldStr))
            f = open(path, 'w')  # We open the files with the WRITE option
            f.write(strg)  # We are writing the the changes to the files
            f.close()  # Closing the files

            for dirpath, dirname, filename in os.walk(new_source_path):

                changes = {"Utabit": changesDict["Utabit"], "UTABIT": changesDict["UTABIT"],
                           "utabit": changesDict["utabit"]}
                for fname in filename:
                    for key in changes.keys():
                        if key in fname:
                            rename(dirpath, key, changes[key])

            print "%s edited!" %type



def edit_android_code(currency_id, changesDict):


    def rename(path, oldstr, newstr):
        for files in os.listdir(path):
            os.rename(os.path.join(path, files), os.path.join(path, files.replace(oldstr, newstr)))



    print "start editing ANDROID ..."

    source_code_path = "./sources/android"
    new_source_path = "./sources/newandroid-%s" %currency_id
    shutil.copytree(source_code_path, new_source_path)
    print "copied tree!"
    for dirpath, dirname, filename in os.walk(new_source_path):  # Getting a list of the full paths of files

        for fname in filename:
            path = os.path.join(dirpath, fname)  # Joining dirpath and filenames
            f = open(path)
            strg = f.read() # Opening the files for reading only
            f.close()
            for oldStr, newStr in changesDict.items():
                try:
                    strg = strg.replace(oldStr, newStr)
                except Exception:
                    print type(strg)
                    pass
                    #print("failed at edit core")
                    #print(type(oldStr))
            f = open(path, 'w')  # We open the files with the WRITE option
            f.write(strg)  # We are writing the the changes to the files
            f.close()  # Closing the files


    for dirpath, dirname, filename in os.walk(new_source_path):

        changes = {"Utabit" : changesDict["Utabit"], "UTABIT" : changesDict["UTABIT"], "utabit" : changesDict["utabit"]}
        for fname in filename:
            for key in changes.keys():
                if key in fname :
                    rename(dirpath, key, changes[key])

    print "ANDROID edited!!"


def get_dnsseeds_pattern(lstDnsSeeds):

    result = ""
    pattern = 'vSeeds.push_back(CDNSSeedData("%s", "%s"));\n'
    for dnsSeed in lstDnsSeeds :
        result += pattern %(dnsSeed.domain, dnsSeed.subDomain+"."+dnsSeed.domain)
    return result

def get_dnsseeds_array(lstDnsSeeds) :

    result = ""
    pattern = '"%s.%s", '
    for dnsSeed in lstDnsSeeds:
        result += pattern %(dnsSeed.subDomain, dnsSeed.domain)

    return result



def get_fullnodes_pattern(lstFullNodes, port):

    result = ""
    pattern = '{{%s}, %s},\n'
    for fullNode in lstFullNodes :
        result += pattern %(fullNode.address, port)
    return result

def build_result(request):
    data = eval(request.body)

    result = 0
    for item in data:
        if item[0] == "request_id":
            request_id = item[1]
        elif item[0] == "platform":
            platformName = item[1]
        else :
            result += int(item[1])

    currency = CryptoCurrency.objects.get(id=request_id)
    platform = Platform.objects.get(cryptoCurrency=currency, name=platformName)

    if result :

        platform.buildStatus = 3
        platform.save()

    else:

        platform.buildStatus = 2
        t = threading.Thread(target=asnibleApacheServer, args=[currency.owner.username, currency.downloadPassword, request_id, platform.name])
        t.daemon = True
        t.start()
        platform.downloadUrl = "%s/%s/%s/%s.zip" %(constants.DOWNLOAD_HOST_URL, currency.owner.username, request_id, platform.name)
        platform.save()


        return HttpResponse("ops!")



def gblock_received(request):

    print "genesis generated"
    print request.body

    data = eval(request.body)
    gdata = data["genesis block"]

    cc = CryptoCurrency.objects.get(id=data["id"])

    print "cc descreiption updated!!"

    gb = GenesisBlock(pszTimestamp=gdata["psztimestamp"], coinBase=gdata["coinbase"], nBits=gdata["nbits"],
                      mHash=gdata["mhash"], nTime=gdata["ntime"],nNonce=gdata["nonce"],
                      pubKey=gdata["pubkey"], gHash=gdata["ghash"], type=data["type"], time=data["time"],
                      cryptoCurrency=cc)
    gb.save()
    print "gb saved"

    cc.description = constants.PROCESSING_EDIT_CORE
    cc.save()


    fullNodes = FullNode.objects.all()
    dnsSeeds = DnsSeed.objects.all()


    for type_core in ["core","core+"] :
        edit_core_code(cc.id, type_core, {
                        constants.CORE_FLAGS["maxMoney"]:cc.maxMoney,
                        constants.CORE_FLAGS["pszTimestamp"]:cc.pszTimestamp,
                        constants.CORE_FLAGS["halvingInterval"]: cc.halvingInterval,
                        constants.CORE_FLAGS["nDefaultPort"]:cc.nDefaultPort,
                        constants.CORE_FLAGS["nTime"]:cc.nTime,
                        constants.CORE_FLAGS["nNonce"]:gb.nNonce,
                        constants.CORE_FLAGS["nBits"]:cc.nBits,
                        constants.CORE_FLAGS["gHash"]:gb.gHash,
                        constants.CORE_FLAGS["mHash"]:gb.mHash,
                        constants.CORE_FLAGS["dnsSeeds"]:get_dnsseeds_pattern(dnsSeeds),
                        constants.CORE_FLAGS["coinBase"]:cc.coinBase,
                        constants.CORE_FLAGS["fullNodes"]:get_fullnodes_pattern(fullNodes, cc.nDefaultPort),
                        constants.CORE_FLAGS["nSubsidy"]:cc.nSubsidy,
                        "Utabit":cc.currencyName.title(), "UTABIT":cc.currencyName.upper(), "utabit":cc.currencyName,
                        "UTB":cc.currencyUnit.upper(), "utb ":cc.currencyUnit,
                        "the Utabit Core developers":"the Bitcoin Core developers",
                        "The Utabit Core developers":"The Bitcoin Core developers",
                        "The Utabit developers":"The Bitcoin developers",
                        "the Utabit developers":"the Bitcoin developers"
                       })

    edit_seeder_code(cc.id, {
                                constants.SEEDER_FLAGS["defPort"]:cc.nDefaultPort,
                                constants.SEEDER_FLAGS["testDefPort"]:"",
                                constants.SEEDER_FLAGS["dnsSeeds"]:get_dnsseeds_array(dnsSeeds)
                            })

    edit_android_code(cc.id, {

                    constants.CORE_FLAGS["maxMoney"]: cc.maxMoney,
                    constants.CORE_FLAGS["nDefaultPort"]: cc.nDefaultPort,
                    constants.CORE_FLAGS["nTime"]: gb.nTime,
                    constants.CORE_FLAGS["nBits"]: cc.nBits,
                    constants.CORE_FLAGS["gHash"]: gb.gHash,
                    constants.CORE_FLAGS["dnsSeeds"]: get_dnsseeds_array(dnsSeeds),

                    "Utabit": cc.currencyName.title(),
                    "UTABIT": cc.currencyName.upper(),
                    "utabit": cc.currencyName,

                    })

    cc.description = constants.PROCESSING_GIT_PUSH
    cc.save()
    push_on_github(cc)

    return HttpResponse("ops!")

def makePassword():

    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    password = "".join(random.sample(s, passlen))
    return  password

class CryptoCurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FullNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FullNode.objects.all()
    serializer_class = FullNodeSerializer



class DnsSeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DnsSeed.objects.all()
    serializer_class = DnsSeedSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def make_hash(params):
    temp = "-".join(params)
    hashedTemp = hashlib.sha1(temp).hexdigest()
    return hashedTemp


