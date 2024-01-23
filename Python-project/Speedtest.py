#pip install pyspeedtest
#pip install speedtest
#pip install speedtest-cli

#method 1
import speedtest

speedTest = speedtest.Speedtest()
print(speedTest.get_best_server())


#check download speed
print(speedTest.download())


#check upload speed
print(speedTest.upload())




#method 2
import pyspeedtest
st = pyspeedtest.SpeedTest()
st.ping()
st.download()
st.upload()