import  tkinter as  tk
import  WeiXiuClassSqlDB as sql
import  tkinter.messagebox as messagebox
import  datetime
#寫錯了，應該是維修。。。。。。。
class BaoFei(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.pc_no=tk.StringVar()
        self.pc_nm=tk.StringVar()
        self.pf_date=tk.StringVar()
        self.address=tk.StringVar()
        self.yt=tk.StringVar()
        self.spec=tk.StringVar()
        self.gb_date=tk.StringVar()
        self.master_emp=tk.StringVar()
        self.gs_type=tk.StringVar()
        self.bz=tk.StringVar()



        self.con_person=tk.StringVar()
        self.con_phone=tk.StringVar()
        self.sx_date=tk.StringVar()
        self.sx_cust=tk.StringVar()

        #保存時賦值
        self.question=tk.StringVar()
        self.status=tk.StringVar()
        self.upddate=tk.StringVar()



        self.createPage()
    #檢查日期格式是否正確
    def checkdate(self):
        try:
            datetime.datetime.strptime(self.sx_date.get(), '%Y%m%d')
            return True
        except:
            return False





    def checknull(self):
        if not self.pc_no.get():
            messagebox.showinfo("","請先查詢出設備編號")
            return  False
        if not self.con_person:
            messagebox.showinfo("", "請輸入聯絡人")
            return False
        if not self.pc_no.get():
            messagebox.showinfo("","請輸入送修日期")
            return  False
        if not self.con_person:
            messagebox.showinfo("", "請輸入聯絡電話")
            return False
        if not self.con_person:
            messagebox.showinfo("", "請輸入送修廠商")
            return False
        if not self.checkdate():
            messagebox.showinfo("", "請輸入八位有效日期")
            return False
        return  True


    def createPage(self):

        def reset():
            self.pc_no.set("")
            self.pc_nm.set("")
            self.pf_date.set("")
            self.address.set("")
            self.yt.set("")
            self.spec.set("")
            self.gb_date.set("")
            self.master_emp.set("")
            self.gs_type.set("")
            self.bz.set("")
            self.con_person.set("")
            self.con_phone.set("")
            self.sx_date.set("")
            self.sx_cust.set("")
            self.question.set("")
            btn_save.config(state="disable")  # 不可编辑
            btn_search.config(state="normal")  # 不可编辑
            txt_question.delete("1.0", tk.END)


        def search():
            dict = sql.WeiXiuSql().search(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.pf_date.set(dict["peifa_date"])
                self.address.set(dict["address"])
                self.yt.set(dict["use_type"])
                self.bz.set(dict["pspec"])
                self.spec.set(dict["p_spec"])
                self.gb_date.set(dict["guobao_date"])
                self.master_emp.set(dict["master_empno"])
                self.gs_type.set(dict["own_type"])
                btn_save.config(state="normal")  # 不可编辑

                self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                messagebox.showinfo("", "沒有此設備編號或已經送修沒結案")

        def save():
            self.question.set(txt_question.get('1.0',tk.END))
            self.status.set("10")
            self.upddate.set(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
            flag=self.checknull()
            if flag:
                sql.WeiXiuSql().insert(self)
                # reset()


        frm1 = tk.Frame(self)

        btn_reset = tk.Button(frm1, text="重置", command=reset)
        btn_reset.grid(row=0,column=3,padx=10)

        btn_search = tk.Button(frm1, text="查询",command=search)
        btn_search.grid(row=0,column=4,padx=10)

        btn_save = tk.Button(frm1, text="保存",command=save)
        btn_save.config(state="disable")  # 不可编辑
        btn_save.grid(row=0,column=5,padx=10)





        frm1.grid(row=0, column=0)

        frm2 = tk.Frame(self)
        tk.Label(frm2, text="设备编号").grid(row=0, column=0)
        tk.Label(frm2, text="设备名称").grid(row=1, column=0)
        tk.Label(frm2, text="配发日期").grid(row=2, column=0)
        tk.Label(frm2, text="地点").grid(row=3, column=0)
        tk.Label(frm2, text="用途").grid(row=4, column=0)
        tk.Label(frm2, text="备注").grid(row=5, column=0)
        tk.Label(frm2, text="联络人").grid(row=6, column=0)
        tk.Label(frm2, text="送修日期").grid(row=7, column=0)
        tk.Label(frm2, text="故障问题描述").grid(row=8, column=0)




        def searchpc(event):
            dict = sql.WeiXiuSql().search(self.pc_no.get().strip())
            if (len(dict) > 0):
                self.pc_nm.set(dict["pc_name"])
                self.pf_date.set(dict["peifa_date"])
                self.address.set(dict["address"])
                self.yt.set(dict["use_type"])
                self.bz.set(dict["pspec"])
                self.spec.set(dict["p_spec"])
                self.gb_date.set(dict["guobao_date"])
                self.master_emp.set(dict["master_empno"])
                self.gs_type.set(dict["own_type"])
                btn_save.config(state="normal")  # 不可编辑

                self.sx_date.set(str(datetime.datetime.now().strftime("%Y%m%d")))
            else:
                messagebox.showinfo("", "沒有此設備編號或已經送修沒結案")

        txt_pc_no=tk.Entry(frm2,textvariable=self.pc_no)
       # txt_pc_no.config(state="disable")
        txt_pc_no.grid(row=0, column=1)
        txt_pc_no.bind("<Return>", searchpc)


        txt_pc_nm=tk.Entry(frm2,textvariable=self.pc_nm)
        txt_pc_nm.config(state="disable")
        txt_pc_nm.grid(row=1, column=1)

        txt_pf_date=tk.Entry(frm2,textvariable=self.pf_date)
        txt_pf_date.config(state="disable")
        txt_pf_date.grid(row=2, column=1)


        txt_address=tk.Entry(frm2,textvariable=self.address)
        txt_address.config(state="disable")
        txt_address.grid(row=3, column=1)


        txt_yt=tk.Entry(frm2,textvariable=self.yt)
        txt_yt.config(state="disable")
        txt_yt.grid(row=4, column=1)


        txt_bz=tk.Entry(frm2, width=50,textvariable=self.bz)
        txt_bz.config(state="disable")
        txt_bz.grid(row=5, column=1,sticky=tk.E,columnspan=3)



        tk.Entry(frm2, text="联络人",textvariable=self.con_person).grid(row=6, column=1)


        tk.Entry(frm2, text="送修日期",textvariable=self.sx_date).grid(row=7, column=1)


        txt_question=tk.Text(frm2,width=50,height=10)
        txt_question.grid(row=8, column=1,columnspan=3,pady=10)


        tk.Label(frm2, text="规格").grid(row=1, column=2)
        tk.Label(frm2, text="过保日期").grid(row=2, column=2)
        tk.Label(frm2, text="保管主管").grid(row=3, column=2)
        tk.Label(frm2, text="归属分类").grid(row=4, column=2)
        tk.Label(frm2, text="联络电话").grid(row=6, column=2)
        tk.Label(frm2, text="送修厂商").grid(row=7, column=2)
        # tk.Label(frm2, text="送修日期").grid(row=7, column=2)



        txt_spec=tk.Entry(frm2,textvariable=self.spec)
        txt_spec.config(state="disable")
        txt_spec.grid(row=1, column=3)



        txt_gb_date=tk.Entry(frm2,textvariable=self.gb_date)
        txt_gb_date.config(state="disable")
        txt_gb_date.grid(row=2, column=3)



        txt_master_emp=tk.Entry(frm2,textvariable=self.master_emp)
        txt_master_emp.config(state="disable")
        txt_master_emp.grid(row=3, column=3)

        txt_gs=tk.Entry(frm2,textvariable=self.gs_type)
        txt_gs.config(state="disable")
        txt_gs.grid(row=4, column=3)


        tk.Entry(frm2,textvariable=self.con_phone).grid(row=6, column=3)
        tk.Entry(frm2,textvariable=self.sx_cust).grid(row=7, column=3)


        # tk.Entry(frm2, text="送修日期").grid(row=7, column=3)




        frm2.grid(row=2, column=0,sticky=tk.W)










        # frm3 = tk.Frame(self)
        # tk.Label(frm3, text="规格").grid(row=0, column=0)
        # tk.Label(frm3, text="过保日期").grid(row=1, column=0)
        # tk.Label(frm3, text="保管主管").grid(row=2, column=0)
        # tk.Label(frm3, text="归属分类").grid(row=3, column=0)
        # tk.Label(frm3, text="联络电话").grid(row=4, column=0)
        # tk.Label(frm3, text="送修厂商").grid(row=5, column=0)
        # tk.Label(frm3, text="送修日期").grid(row=6, column=0)
        #
        # tk.Entry(frm3, text="设备编号").grid(row=0, column=1)
        # tk.Entry(frm3, text="设备名称").grid(row=1, column=1)
        # tk.Entry(frm3, text="配发日期").grid(row=2, column=1)
        # tk.Entry(frm3, text="地点").grid(row=3, column=1)
        # tk.Entry(frm3, text="用途").grid(row=4, column=1)
        # tk.Entry(frm3, text="联络人").grid(row=5, column=1)
        # tk.Entry(frm3, text="送修日期").grid(row=6, column=1)
        #
        # frm3.grid(row=2, column=1)






        #Entry(self.root, textvariable=self.username).pack()
        # ck1 = Checkbutton(self.root, variable=self.password, onvalue="T", offvalue="F")
        # def chang(event):
        #     print(self.password.get())
        # ck1.bind("<Button-1>", chang)
        # ck1.pack()