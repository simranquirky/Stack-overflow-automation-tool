import shlex
from subprocess import Popen, PIPE
import requests
import webbrowser

def getData(cmd):
	args = shlex.split(cmd)
	process = Popen(args, stdout = PIPE, stderr = PIPE)
	output, error = process.communicate()
	return output, error
def make_request(error):
	print("Searching for " + error)
	response = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(error))
	return response.json()
def get_urls(json_dict):
	url_list = []
	count = 0
	for i in json_dict["items"]:
		if i["is_answered"]:
			url_list.append(i["link"])
		count += 1
		if count == 3:
			break
	for i in url_list:
		webbrowser.open(i)

filePath=input("Enter the python file name you want to check:")

if __name__ == "__main__":
	output, error = getData("python {}".format(filePath))
	error = error.decode("utf-8").strip().split("\r\n")[-1]
	print("Error => ",error)
	if(error):
		error_list = error.split(":",1)
		json1 = make_request(error_list[0])
		json2 = make_request(error_list[1])
		json3 = make_request(error)
		get_urls(json1)
		get_urls(json2)
		get_urls(json3)
	else:
		print("No Error")
