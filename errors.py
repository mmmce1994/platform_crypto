node is off :

{'msg': u'ERROR! SSH encountered an unknown error during the connection. We recommend you re-run the command using -vvvv, which will enable SSH debugging output to help diagnose the issue', 'unreachable': True, 'changed': False}


invalid platform name

{u'cmd': u'docker run -e GIT_URL=https://github.com/mirzaei-ce/core-outbit -e PLATFORM=core -e ID=14 --name 14 -v /home/mhghasemi/shared/14/core:/share -i core-builder:0.4', u'stdout': u'dGFsZWdoYW5pX29mZmljZQ== url_defined 0\ndGFsZWdoYW5pX29mZmljZQ== request_id 14\ndGFsZWdoYW5pX29mZmljZQ== platform core\ndGFsZWdoYW5pX29mZmljZQ== platform_defined 0\ndGFsZWdoYW5pX29mZmljZQ== provided_platform_isvalid 400\ndGFsZWdoYW5pX29mZmljZQ== id_defined 0', u'warnings': [], u'delta': u'0:00:04.506480', 'stdout_lines': [u'dGFsZWdoYW5pX29mZmljZQ== url_defined 0', u'dGFsZWdoYW5pX29mZmljZQ== request_id 14', u'dGFsZWdoYW5pX29mZmljZQ== platform core', u'dGFsZWdoYW5pX29mZmljZQ== platform_defined 0', u'dGFsZWdoYW5pX29mZmljZQ== provided_platform_isvalid 400', u'dGFsZWdoYW5pX29mZmljZQ== id_defined 0'], u'end': u'2017-11-02 18:44:38.357527', '_ansible_no_log': False, u'start': u'2017-11-02 18:44:33.851047', u'changed': True, 'failed': True, u'stderr': u'', u'rc': 1, 'invocation': {'module_name': u'command', u'module_args': {u'warn': True, u'executable': None, u'chdir': None, u'_raw_params': u'docker run -e GIT_URL=https://github.com/mirzaei-ce/core-outbit -e PLATFORM=core -e ID=14 --name 14 -v /home/mhghasemi/shared/14/core:/share -i core-builder:0.4', u'removes': None, u'creates': None, u'_uses_shell': True}}}



container busy

{u'cmd': u'docker run -e GIT_URL=https://github.com/mirzaei-ce/core-outbit -e PLATFORM=linux -e ID=14 --name 14 -v /home/mhghasemi/shared/14/linux:/share -i core-builder:0.4', u'stdout': u'', u'warnings': [], u'delta': u'0:00:00.009530', 'stdout_lines': [], u'end': u'2017-11-02 18:53:09.931071', '_ansible_no_log': False, u'start': u'2017-11-02 18:53:09.921541', u'changed': True, 'failed': True, u'stderr': u'docker: Error response from daemon: Conflict. The container name "/14" is already in use by container "9b8ad03fd533bc588bed368a760f1267ff03a81d7b8f2f38886ba408ee562c59". You have to remove (or rename) that container to be able to reuse that name.\nSee \'docker run --help\'.', u'rc': 125, 'invocation': {'module_name': u'command', u'module_args': {u'warn': True, u'executable': None, u'chdir': None, u'_raw_params': u'docker run -e GIT_URL=https://github.com/mirzaei-ce/core-outbit -e PLATFORM=linux -e ID=14 --name 14 -v /home/mhghasemi/shared/14/linux:/share -i core-builder:0.4', u'removes': None, u'creates': None, u'_uses_shell': True}}}





uilder/linux/depends/x86_64-unknown-linux-gnu/bin'", 
            "libtool: install: /usr/bin/install -c outbitd /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/outbitd", 
            "libtool: install: /usr/bin/install -c outbit-cli /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/outbit-cli", 
            "libtool: install: /usr/bin/install -c outbit-tx /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/outbit-tx", 
            "libtool: install: /usr/bin/install -c wallet-utility /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/wallet-utility", 
            "libtool: install: /usr/bin/install -c test/test_outbit /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/test_outbit", 
            "libtool: install: /usr/bin/install -c bench/bench_outbit /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/bench_outbit", 
            "libtool: install: /usr/bin/install -c qt/outbit-qt /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/outbit-qt", 
            "libtool: install: /usr/bin/install -c qt/test/test_outbit-qt /share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/bin/test_outbit-qt", 
            " /bin/mkdir -p '/share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/include'", 
            " /usr/bin/install -c -m 644 script/outbitconsensus.h '/share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/include'", 
            "make[3]: Leaving directory `/builder/linux/src'", 
            "make[2]: Leaving directory `/builder/linux/src'", 
            "make[1]: Leaving directory `/builder/linux/src'", 
            "make[1]: Entering directory `/builder/linux'", 
            "make[2]: Entering directory `/builder/linux'", 
            "make[2]: Nothing to be done for `install-exec-am'.", 
            " /bin/mkdir -p '/share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/lib/pkgconfig'", 
            " /usr/bin/install -c -m 644 liboutbitconsensus.pc '/share/linux/builder/linux/depends/x86_64-unknown-linux-gnu/lib/pkgconfig'", 
            "make[2]: Leaving directory `/builder/linux'", 
            "make[1]: Leaving directory `/builder/linux'", 
            "dGFsZWdoYW5pX29mZmljZQ== url_defined 0", 
            "dGFsZWdoYW5pX29mZmljZQ== make_install_done 0", 
            "dGFsZWdoYW5pX29mZmljZQ== request_id 14", 
            "dGFsZWdoYW5pX29mZmljZQ== auto_generate_done 0", 
            "dGFsZWdoYW5pX29mZmljZQ== platform linux", 
            "dGFsZWdoYW5pX29mZmljZQ== platform_defined 0", 
            "dGFsZWdoYW5pX29mZmljZQ== provided_url_isvalid 0", 
            "dGFsZWdoYW5pX29mZmljZQ== provided_platform_isvalid 0", 
            "dGFsZWdoYW5pX29mZmljZQ== source_cloned 0", 
            "dGFsZWdoYW5pX29mZmljZQ== configuration_done 0", 
            "dGFsZWdoYW5pX29mZmljZQ== make_done 0", 
            "dGFsZWdoYW5pX29mZmljZQ== id_defined 0"
        ], 
        "warnings": []
    }
}
{
    "testserver": {
        "cmd": "docker ps", 
        "end": "2017-11-02 19:13:06.719780", 
        "_ansible_no_log": false, 
        "stdout": "CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES", 
        "changed": true, 
        "start": "2017-11-02 19:13:06.709878", 
        "delta": "0:00:00.009902", 
        "stderr": "", 
        "rc": 0, 
        "invocation": {
            "module_name": "command", 
            "module_args": {
                "creates": null, 
                "executable": null, 
                "chdir": null, 
                "_raw_params": "docker ps", 
                "removes": null, 
                "warn": true, 
                "_uses_shell": true
            }
        }, 
        "stdout_lines": [
            "CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES"
        ], 
        "warnings": []
    }
}
{
    "testserver": {
        "cmd": "echo ooooooooooooofinish", 
        "end": "2017-11-02 19:13:06.908022", 
        "_ansible_no_log": false, 
        "stdout": "ooooooooooooofinish", 
        "changed": true, 
        "start": "2017-11-02 19:13:06.906933", 
        "delta": "0:00:00.001089", 
        "stderr": "", 
        "rc": 0, 
        "invocation": {
            "module_name": "command", 
            "module_args": {
                "creates": null, 
                "executable": null, 
                "chdir": null, 
                "_raw_params": "echo ooooooooooooofinish", 
                "removes": null, 
                "warn": true, 
                "_uses_shell": true
            }
        }, 
        "stdout_lines": [
            "ooooooooooooofinish"
        ], 
        "warnings": []
    }


