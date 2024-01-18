import tkinter as tk
from tkinter import messagebox

def on_calculate():
    num1 = entry1.get()
    num2 = entry2.get()
    operation = operation_var.get()

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Error", "0으로 나눌 수 없습니다.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected")
            return

        result_var.set(str(result))

    except ValueError:
        messagebox.showerror("Error", "유효하지 않은 숫자 입력")

# GUI 생성
root = tk.Tk()
root.title("Simple Calculator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

entry1 = tk.Entry(frame, width=10)
entry2 = tk.Entry(frame, width=10)
operation_var = tk.StringVar(frame)
operation_var.set("add")  # default value
operation_menu = tk.OptionMenu(frame, operation_var, "add", "subtract", "multiply", "divide")
result_var = tk.StringVar(frame)
result_var.set("결과가 여기에 표시됩니다.")
result_label = tk.Label(frame, textvariable=result_var)

calculate_button = tk.Button(frame, text="계산", command=on_calculate)

entry1.grid(row=0, column=0)
operation_menu.grid(row=0, column=1)
entry2.grid(row=0, column=2)
calculate_button.grid(row=1, column=1, pady=10)
result_label.grid(row=2, column=1, pady=10)

root.mainloop()

"""
import tkinter as tk
from tkinter import messagebox

# tkinter의 Tk 클래스는 주 윈도우 또는 최상위 윈도우를 생성한다.
root = tk.Tk()

# title() 메서드를 사용하여 윈도우의 제목을 설정할 수 있다.
root.title("tkinter Introduction")

# Label 위젯은 텍스트나 이미지를 표시할 때 사용한다.
label = tk.Label(root, text="This is a label.")
label.pack()

# Button 위젯은 클릭 가능한 버튼을 생성한다.
# command 매개변수는 버튼이 클릭될 때 호출될 함수를 지정한다.
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked!"))
button.pack()

# Entry 위젯은 한 줄의 텍스트 입력을 받을 때 사용한다.
entry = tk.Entry(root)
entry.pack()

# Text 위젯은 여러 줄의 텍스트 입력을 받을 때 사용한다.
text = tk.Text(root, height=5, width=30)
text.pack()

# Listbox 위젯은 목록을 표시하고 목록에서 항목을 선택할 수 있다.
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack()

# Checkbutton 위젯은 체크박스를 생성한다.
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check Me!", variable=check_var)
checkbutton.pack()

# Radiobutton 위젯은 라디오 버튼을 생성한다.
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="A")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="B")
radio1.pack()
radio2.pack()

# Spinbox 위젯은 특정 범위의 숫자를 선택할 수 있는 박스를 생성한다.
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# Scale 위젯은 슬라이더를 생성하여 값의 범위를 선택할 수 있다.
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# messagebox는 다양한 팝업 대화상자를 제공한다.
# 예: 정보, 경고, 에러 메시지 등을 표시할 때 사용한다.
messagebox.showinfo("Info", "This is an info message.")

root.mainloop()  # GUI를 실행하고 사용자의 이벤트를 기다린다.

"""