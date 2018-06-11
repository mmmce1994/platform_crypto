from ansible.plugins.callback import CallbackBase
import json
import sys
import requests




class ResultsCollector(CallbackBase):

    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}




    def v2_runner_on_ok(self, result, **kwargs):




        def get_data_from_text(txt):

            txt = txt.replace("\\\"", "'")
            if "stdout_lines" in txt:
                print "miad"
                txt = txt[txt.find("stdout_lines"):]
                start = txt.find("{")
                end = txt.find("'}\"")
                data = eval(txt[start:end + 2])
                print(data)
                r = requests.get("http://localhost:8000/new_gb", json = data)


            else:
                return
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print json.dumps({host.name: result._result}, indent=4)
        get_data_from_text(json.dumps({host.name: result._result}, indent=4))


