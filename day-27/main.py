from tkinter import *

# def button_clicked():
#     data_1 = input.get()
#     miles_label.config(text=data_1)
# def get_input():
#     user_input =entry.get()
#     print(user_input)
def mile_to_km_converter():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text = f"{km}")


window = Tk()
window.title("Miles To Km Converter")
window.minsize(width=500,height =300)
window.config(padx = 20 , pady =20)


# #Label
miles_input = Entry(width = 7)
miles_input.grid(column=1, row =0)
# button = Button(command = get_input)
# button.grid(column=1,row = 3)

miles_label = Label(text ="Miles", font = ("Arial",18,"bold"))
miles_label.grid(column = 2, row = 0)
is_equal_label = Label(text ="is equal to", font = ("Arial", 18, "bold"))
is_equal_label.grid(column = 0, row = 1)
km_result_label = Label(text= "0",font = ("Arial", 18, "bold"))
km_result_label.grid(column =1 ,row =1)
km_label = Label(text ="km", font = ("Arial", 18, "bold"))
km_label.grid(column = 2, row = 1)
calculate_button = Button(text = "Calculate", command = mile_to_km_converter)
calculate_button.grid(column=1,row = 2)



#
# new_button = Button(text = "Don't Click", command = button_clicked)
# new_button.grid(column =2,row = 0)
# # Entry
# # input = Entry(width = 10)
# # input.get()
# # input.grid(column=)
#
# entry = Entry(width = 30)
#
#


window.mainloop()