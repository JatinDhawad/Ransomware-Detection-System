import tkinter as tk
from tkinter import messagebox
import main
import threading
import winsound
import os

app_state = {"attack_active": False}


def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)


def set_buttons(state):
    attack_btn.config(state=state)
    recover_btn.config(state=state)


def show_ransom_message():
    ransom = tk.Toplevel()
    ransom.title("⚠️ Simulated Ransomware Payload")
    ransom.geometry("400x250")
    ransom.config(bg="black")

    tk.Label(
        ransom,
        text="SIMULATED RANSOMWARE MESSAGE",
        fg="red",
        bg="black",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Label(
        ransom,
        text="Educational Simulation Only\nRecover before timer expires",
        fg="white",
        bg="black",
        font=("Arial", 10)
    ).pack(pady=5)

    timer_label = tk.Label(
        ransom,
        text="Time left: 60",
        fg="yellow",
        bg="black",
        font=("Arial", 12, "bold")
    )
    timer_label.pack(pady=10)

    time_left = 60

    def countdown():
        nonlocal time_left

        if not app_state["attack_active"]:
            ransom.destroy()
            return

        if time_left >= 0:
            timer_label.config(text=f"Time left: {time_left}")
            time_left -= 1
            ransom.after(1000, countdown)
        else:
            delete_files_one_by_one()

    def delete_files_one_by_one():
        files = [f for f in os.listdir("test_data") if f.endswith(".locked")]

        def delete_next():
            if files:
                file = files.pop(0)
                path = os.path.join("test_data", file)

                try:
                    os.remove(path)
                    log(f"💣 Deleted: {file}")
                except:
                    pass

                ransom.after(1000, delete_next)
            else:
                messagebox.showerror(
                    "Data Lost",
                    "Encrypted files have been deleted!"
                )
                ransom.destroy()

                app_state["attack_active"] = False
                files_label.config(text="Files Affected: 0")
                recover_btn.config(state="disabled")
                status_label.config(text="Status: Data Lost", fg="red")

        delete_next()

    countdown()


def start_attack():
    def run():
        app_state["attack_active"] = True

        set_buttons("disabled")
        status_label.config(text="⚠️ Attack Running", fg="orange")

        detected, files = main.detect()

        files_label.config(text=f"Files Affected: {files}")

        if detected == "recovery_required":
            app_state["attack_active"] = False

            messagebox.showwarning(
                "Recovery Required",
                "Recover encrypted files before starting a new attack."
            )

            log("⚠️ Recovery required before new attack.")
            status_label.config(text="Recovery Required", fg="orange")

        elif detected:
            winsound.Beep(1000, 500)

            status_label.config(text="🚨 Threat Detected", fg="red")

            recover_btn.config(state="normal")

            show_ransom_message()

            messagebox.showwarning(
                "Alert",
                f"Ransomware Detected!\nFiles affected: {files}"
            )

            log(f"🚨 Detected | Files affected: {files}")

        else:
            app_state["attack_active"] = False

            status_label.config(text="✅ Safe", fg="green")

            log("System safe")

        attack_btn.config(state="normal")

    threading.Thread(target=run).start()


def recover_files():
    key_window = tk.Toplevel()
    key_window.title("Enter Decryption Key")
    key_window.geometry("300x150")

    tk.Label(
        key_window,
        text="Enter Decryption Key:"
    ).pack(pady=5)

    key_entry = tk.Entry(key_window, width=30)
    key_entry.pack(pady=5)

    def submit_key():
        user_key = key_entry.get()

        result = main.recover(user_key)

        if result == -1:
            messagebox.showerror("Error", "Invalid key format!")

        elif result == -2:
            messagebox.showerror("Error", "Wrong decryption key!")

        else:
            app_state["attack_active"] = False

            status_label.config(text="🔓 Files Recovered", fg="blue")

            files_label.config(text="Files Affected: 0")

            recover_btn.config(state="disabled")

            messagebox.showinfo(
                "Success",
                f"Recovered {result} files"
            )

            log(f"Recovered {result} files")

        key_window.destroy()

    tk.Button(
        key_window,
        text="Submit",
        command=submit_key
    ).pack(pady=10)


root = tk.Tk()
root.title("Ransomware Detection System")
root.geometry("420x420")

tk.Label(
    root,
    text="Cyber Security Dashboard",
    font=("Arial", 16, "bold")
).pack(pady=10)

status_label = tk.Label(
    root,
    text="Status: Idle",
    font=("Arial", 12)
)
status_label.pack()

files_label = tk.Label(
    root,
    text="Files Affected: 0",
    font=("Arial", 12)
)
files_label.pack(pady=5)

attack_btn = tk.Button(
    root,
    text="Start Attack",
    command=start_attack,
    width=22
)
attack_btn.pack(pady=10)

recover_btn = tk.Button(
    root,
    text="Recover Files",
    command=recover_files,
    width=22,
    state="disabled"
)
recover_btn.pack(pady=5)

tk.Label(
    root,
    text="Logs:",
    font=("Arial", 12, "bold")
).pack()

log_box = tk.Text(
    root,
    height=12,
    width=48
)
log_box.pack(pady=10)

root.mainloop()