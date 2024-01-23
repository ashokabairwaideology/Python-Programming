import speedtest
st = speedtest.Speedtest()
print(st.download())
print(st.upload())
print(st.results.ping)



#pip install speedtest-cli