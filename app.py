from urllib.request import urlopen
import webbrowser
#feaching html of time.com
url = "http://time.com"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
#writing code to html page
f = open('page.html', 'w')
f.write(str(html))
f.close()
f = open('page.html','a')
#adding dom manipulation code to html file to get the result
f.write('<script> console.warn = () => {}; const collection = document.getElementsByClassName("latest-stories__item"); a = []; for(i =0; i<collection.length; i++){ b = collection[i].getElementsByTagName("a")[0].href.split("/");  let userObj = { "title": collection[i].getElementsByTagName("h3")[0].innerText, "link": "https://time.com/"+b[b.length - 3]+"/"+b[b.length -2]};a.push(userObj);}console.log(a);const element = document.querySelector("body");element.innerHTML = JSON.stringify(a);console.clear(); </script>')
# print("It will take time to run.\nPlease wait")
print("Please run page.html and please save html before run\nnot get result then try to save the html file again and check")
# webbrowser.open_new_tab('page.html')

