from ansible.plugins.callback import CallbackBase
import json, requests


class ResultsCollector(CallbackBase):

    def __init__(self, operationType, *args, **kwargs ):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.operationType = operationType





    def v2_runner_on_ok(self, result, **kwargs):


        def get_builder_data(txt):

            a = txt.find('"First line of process results!"')
            if a != -1 :

                b = txt.find('"Last line of process results!"') + len('"Last line of process results!"')
                temp = txt[a:b].split("\n")
                data = []

                for item in temp:
                    if item.find(",") != -1:
                        item = item.strip()
                        data.append(item[26:len(item) - 2].split(" "))
                    else:
                        data.append(item[26:len(item) - 1].split(" "))

                platform = ""
                for item in data:
                    if item[0] == "platform":
                        platform = item[1]
                        break

                if platform == "android":
                    data = data[1:8]
                else:
                    data = data[1:13]

                print data
                r = requests.get("http://localhost:8000/build_result", json=data)

        def get_data_from_text(txt):

            txt = txt.replace("\\\"", "'")
            if "stdout_lines" in txt:
                print "miad"
                txt = txt[txt.find("stdout_lines"):]
                start = txt.find("{")
                end = txt.find("'}\"")
                data = eval(txt[start:end + 2])
                print(data)
                r = requests.get("http://localhost:8000/new_gb", json=data)




            else:
                pass

        host = result._host
        data = json.dumps({host.name: result._result}, indent=4)

        if self.operationType == "genesisRunner" :
            get_data_from_text(json.dumps({host.name: result._result}, indent=4))

        elif self.operationType in ["coreBuilder", "androidbuilder"]  :
            print data
            get_builder_data(data)





    def v2_runner_on_unreachable(self, result, **kwargs):
        print eval(str(result._result))


    def v2_runner_on_failed(self, result, **kwargs):
        print eval(str(result._result))