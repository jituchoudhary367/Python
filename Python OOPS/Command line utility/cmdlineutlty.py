# #Command line utilities are the program that can be run fromm teh terminal or the command line interface , and they are the an essential part of many development workflows. In Python ,we can create our own command line utilities using built-in "argparse" module. 
# import argparse
# import requests

# def download_file(url,local_filename):
#     local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
# #     return local_filename

# parser = argparse.ArgumentParser()

# #Add commmand line arguments 
# parser.add_argument("url",help ="Url of the file to download")
# parser.add_argument("output",help="by which name do you want to save your file")


# #parse the argument 
# args = parser.parse_args()

# #use the arguments in the code
# print(args.url)
# print(args.output)
# download_file(args.url,args.output)

