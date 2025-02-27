import tkinter 
import psutil

def updateInfo():
    global curr_recv, curr_sent, prev_recv, prev_sent

    cpu_p = psutil.cpu_percent(interval=1) # 매 초 cpu사용량 추출
    listbox1.delete(0, 'end')
    listbox1.insert(0, f"CPU사용량: {cpu_p}%")

    memory = psutil.virtual_memory() # 메모리 정보 추출
    memory_avail = round(memory.available/1024**3,1) # 사용 가능한 메모리 추출
    listbox2.delete(0, 'end')
    listbox2.insert(0, f"사용 가능한 메모리: {memory_avail} GB")


    net = psutil.net_io_counters() # 현재 주고 받은 네트워크 정보 추출
    curr_sent = net.bytes_sent/1024**2 # 현재 보낸 데이터 초기화
    curr_recv = net.bytes_recv/1024**2 # 현재 받은 데이터 초기화

    sent = round(curr_sent-prev_sent,1) # 현재 보낸거 - 이전에 보낸거 계산 후 반올림
    recv = round(curr_recv-prev_recv,1) # 현재 받은거 - 이전에 받은거 계산 후 반올림

    listbox3.delete(0, 'end')
    listbox3.insert(0, f"보낸 데이터: {round(sent, 1)} MB")
    listbox4.delete(0, 'end')
    listbox4.insert(0, f"받은 데이터: {round(recv, 1)} MB")

    prev_sent = curr_sent 
    prev_recv = curr_recv 


    window.after(500, updateInfo)  # 1초마다 업데이트

curr_sent = 0 # 현재 보낸 데이터 초기화
curr_recv = 0 # 현재 받은 데이터 초기화

prev_sent = 0 # 이전에 보낸 데이터 초기화
prev_recv = 0 # 이전에 받은 데이터 초기화

window = tkinter.Tk()
window.title("컴퓨터 상태")
window.geometry("500x300+800+200")
window.resizable(False, False)

listbox1 = tkinter.Listbox(width=50, height=2,)
listbox1.pack()
listbox1.place(x=130, y=20)

listbox2 = tkinter.Listbox(width=50, height=2,)
listbox2.pack()
listbox2.place(x=130, y=95)

listbox3 = tkinter.Listbox(width=50, height=2,)
listbox3.pack()
listbox3.place(x=130, y=165)

listbox4 = tkinter.Listbox(width=50, height=2,)
listbox4.pack()
listbox4.place(x=130, y=235)

label1 = tkinter.Label(text="CPU사용량")
label1.pack()
label1.place(x=30,y=25)

label2 = tkinter.Label(text="사용가능한\n메모리")
label2.pack()
label2.place(x=30,y=100)

label3 = tkinter.Label(text="보낸 데이터")
label3.pack()
label3.place(x=30,y=170)

label4 = tkinter.Label(text="받은 데이터")
label4.pack()
label4.place(x=30,y=235)

updateInfo()

window.mainloop()