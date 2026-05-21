import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
import os
import base64
from io import BytesIO

# ------------------------------------------------------------
# SimpleQR - QR-Code Generator mit GUI
# Benoetigte Pakete:
#   pip install qrcode[pil] pillow
# ------------------------------------------------------------

ICON_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAMAAAADACAMAAABlApw1AAAA7VBMVEX///////29wMBrk9j6+vrI"
    "y83oYFT/yGPp6uprbnRETFTn6OwnMz8uNT5RV14/R1CrrbI5Q0pxdHhbXWPh4uIbIS5QVF7x8vW0"
    "tbegpKU6Qk0sOEAhLzdETVIqMDyWl5mPkZhiZm//zmr/z2NPXHY4SFHtYU7dX1NFR0mLVFbzwGJ6"
    "blhHSVZARD01OkdgfbGNeFVsiczdYmJTbIovSk/dt18MM0mCUU7QYVuAhIgIHioMEiULFSLU1tgk"
    "JTggKDI5PDylYVy/XVpjTlRwj7t3UVArNVG/qmTMq15qZlE8Q1glKkfzy218dVRXXEZpc0VUAAAH"
    "GElEQVR4nO2df4OTNhiAgQWluYOU/rhCWriiVm8O0enNicrqNt2mc/v+H2fcnQcJhF5Caend3uev"
    "60HTPE1a3iRvqKYBAAAAAAAAAAAAAHCn0OXZy6uol7xFtXaBYn3y+s9MSaxt6pUZcpgzVQHkTBfh"
    "QgbXbF//4ToMbRnejpGagHb0Dl8R3MTcb11/lNpYkvdqTZALTDFOQhnwFi3guVLvv4vxtIVAsjTz"
    "zncTRqbWuBwok/qYpUkrgbnXvmbd4tu3WwCBQM+AQN+AQN+AQN+AQN+AQN+AQN+AQN+AgMTp7AO9"
    "6UHlVOnJs64FrMzjMCfs0ZnnMVNdFvdIQ+aQmQOYVQoyJuL5gY4FJim17es5lctZj4HBPHH5S7gs"
    "6oHS9dpnamUcL6JC11rG/KzWIvKEBt0KWCklOGbA2I0nRddAg5iOijcdjSmNikrldpQ4xTRSasf4"
    "7Hri6rIk6hiagG4FzITg1eqcgcRuyggQlxcYoG/HdF5gss6f+CH58KzgjNBUVM9OBfLCYvfXNwy/"
    "/U5wUB6vCUQNAsM5Jq8+Pv+x4GNM3AH3edqNwJycv3zMcO/nFcFtBPIe9Pw7lkdnZLwPAXz+8h7D"
    "k1xAvQX0C4GgKkCjXgRIZwJkXwKPOQEKAiAAArdboLuv0b0J7Oo60JfA2WEKLGQF6Jl6KKEqoLzM"
    "OkvsY1Fseynw5gnLJ9IiFtLFsZBQQDNsGyuvhRrLoVDaC/Hq0/cMnwJMow3htFAg/9sIMXn0iiUO"
    "mKeyzPylqZotcfkqon9mDo2D8xUDDkKjhQAiJCZnJYTGMfVFb3T+/C3WoquFoWHiBmwCAqbrFOmK"
    "A5qLBBpjno/tCJNOQGxxA2yb1FPFjOykxE5Ohsz7UxFw3GRwfbQyHtD0bJAwJeX93FfMSWnHRYNy"
    "cH2tIuDTpPguqwpo1YK66ycbqbem3iigIbOcRhEIVMs5gDSrigBLXeAQKlxFSeAQAYG+AYHds/mb"
    "Y4NAzukhCFSvPvwFqCbAnce3QL2gfVzKrOWgxqgMgisC2Yg774QwAoKCBulWabQyIH9NathRcU2q"
    "BnMudyIOymjUs+sFEft0142A/JDWSKLyOC8wSKrnjrNrAUFBNNy5gDZJR3WYfs13IbN26rfQNR/z"
    "iQpKs13XPx8eWTVmzFfTMlwsmXexdm55DNULsvYUkG7CGno7/yACGzmIqB64q3Q8vbB/bnftL/CW"
    "e7hS7RBvbTs9G+gzY6iEwU5W8eOBmcmf6h3toYvpnty+qW+E4Zrd5MQJWGlSOdcxdh9KoNNQdufU"
    "FXTEVIoTGNmkcq6Lhdkq3WLGKk1ALgTKjnHKrA9ki9yOZZ6fLMxW6ZQ8DJ7Ik52QRoFhgolvTSbW"
    "0RXW0ZhQYbZKj6Bxs4CfEMIP8FO6FwGVb4pcwG0UoFWB0X4EVACBvgGBvgGBvgGB7tGR6d8EM0+n"
    "cCXW99QC3lowpVmhiClVBcSZu52C/GPBpDJPWAwB0JgmjQIhOeMFUluc+NotpnNyA0FUjBqR75x4"
    "WkM4fYK51QA9Lxovd59sIHEjAuZdnJkmO8jiBjSZUZ1EzVRv4LF3DmONbAtAoG9AoG9AoG8OQyAP"
    "55Ys7KKeriNvyCxazjyveW60JyajMOEI47JOurZcL1JmJ9/0l9OmqcWesEY2jvn8AUrLKXM0IOxO"
    "PofQQUXA3xSFdBVKXN7lTBwYmkmwehazU7KrOOF28nFbEWsCeEMYS8WZo7o2MWdqqzt5V06dSLQU"
    "gYb22R9//sTw1+cvxCmPN6ceXwpgbh9mFSrcCKdnkcMG5TIC2tE7YosSmZFvB39/fXi/4OHTF18C"
    "qf0DOeZ04/3G7LU4V2oYkqna8v/VBogGgfj11/sMT19IbkW8IFNYzinLHM7x9EhZIGgQmOPXDx7y"
    "AlhaoBV5t8UdtsCdFJD9DLQDWoAr7E62gPy3UCugC3GFKXehwaEJ1C9k9JYJ4DyUYLh/cyghvv2v"
    "6NbAwnSirrvQRSz0oOTpP/HGzaCjrfMfOhXQPDsg//7A8HkV00HzRrj4JE3L0VuaFuMZ5EdVBqNT"
    "UcjTrcDEyUN6bjIdE7vcNlodD9A4drks5fF1kG5MBRPza2GrdyqAPFzJ2nbtMlVX10auPSpiShRV"
    "M7xpMaT0QsGQZiHKne5WIB/TL8fsbLozYsbtupYNIpMZAESVufdxUegsFUzNjxoGUV0K1JKeKzG8"
    "ZfGPlHKnG8YDHQvsGxDoGxDoGxDoGxDoGxDoGxDoGxDoGxDom5YC4gWOPmjbAnb7n/iRfx0phmEr"
    "ATeV+pWbrX5IZyL1Eku3lQCmUttktll6z8ZSG3LcoIXAO4xjLIN92n6H4ZDKvQbG71V3WSPn7bEc"
    "c6O9QEbCUOpF1o5yR52Zkr91NtnmNkHWjn5QTZHWArd/dysAAAAAAAAAAAAAAP9b/gOfjZGOrcqR"
    "QAAAAABJRU5ErkJggg=="
)


class QRCodeGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("QR-Code Generator")
        self.root.geometry("550x700")
        self.root.resizable(True, True)

        self.qr_image = None
        self.preview_image = None

        self._set_icon()
        self.create_widgets()

    def _set_icon(self):
        try:
            icon_data = base64.b64decode(ICON_BASE64)
            icon_image = Image.open(BytesIO(icon_data))
            self._icon_photo = ImageTk.PhotoImage(icon_image)
            self.root.iconphoto(True, self._icon_photo)
        except Exception:
            pass

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="QR-Code Generator",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=15)

        description = tk.Label(
            self.root,
            text="Beliebigen Text oder URL eingeben und QR-Code erzeugen.",
            font=("Segoe UI", 10)
        )
        description.pack(pady=(0, 15))

        frame_input = tk.Frame(self.root)
        frame_input.pack(fill="x", padx=20)

        label_input = tk.Label(
            frame_input,
            text="Inhalt:",
            font=("Segoe UI", 11, "bold")
        )
        label_input.pack(anchor="w")

        self.text_input = tk.Text(
            frame_input,
            height=6,
            font=("Consolas", 11)
        )
        self.text_input.pack(fill="x", pady=5)

        frame_options = tk.Frame(self.root)
        frame_options.pack(fill="x", padx=20, pady=10)

        tk.Label(
            frame_options,
            text="QR-Groesse:",
            font=("Segoe UI", 10)
        ).grid(row=0, column=0, sticky="w")

        self.size_var = tk.IntVar(value=10)

        size_scale = tk.Scale(
            frame_options,
            from_=4,
            to=20,
            orient="horizontal",
            variable=self.size_var
        )
        size_scale.grid(row=0, column=1, sticky="ew", padx=10)

        frame_options.columnconfigure(1, weight=1)

        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        generate_button = tk.Button(
            frame_buttons,
            text="QR-Code erzeugen",
            command=self.generate_qr,
            width=20,
            height=2,
            bg="#0078D7",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        generate_button.grid(row=0, column=0, padx=10)

        save_button = tk.Button(
            frame_buttons,
            text="QR-Code speichern",
            command=self.save_qr,
            width=20,
            height=2,
            bg="#28A745",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        save_button.grid(row=0, column=1, padx=10)

        preview_label = tk.Label(
            self.root,
            text="Vorschau:",
            font=("Segoe UI", 11, "bold")
        )
        preview_label.pack(anchor="w", padx=20, pady=(20, 5))

        self.preview_area = tk.Label(
            self.root,
            bd=2,
            relief="groove",
            width=400,
            height=400
        )
        self.preview_area.pack(padx=20, pady=10)

        self.status_var = tk.StringVar()
        self.status_var.set("Bereit")

        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            bd=1,
            relief="sunken",
            anchor="w"
        )
        status_bar.pack(side="bottom", fill="x")

    def generate_qr(self):

        data = self.text_input.get("1.0", tk.END).strip()

        if not data:
            messagebox.showwarning(
                "Eingabe fehlt",
                "Bitte Text oder eine URL eingeben."
            )
            return

        try:
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=self.size_var.get(),
                border=4
            )

            qr.add_data(data)
            qr.make(fit=True)

            self.qr_image = qr.make_image(
                fill_color="black",
                back_color="white"
            ).convert("RGB")

            preview = self.qr_image.copy()
            preview.thumbnail((400, 400))

            self.preview_image = ImageTk.PhotoImage(preview)
            self.preview_area.config(image=self.preview_image)
            self.status_var.set("QR-Code erfolgreich erzeugt.")

        except Exception as e:
            messagebox.showerror(
                "Fehler",
                f"QR-Code konnte nicht erzeugt werden:\n\n{e}"
            )

    def save_qr(self):

        if self.qr_image is None:
            messagebox.showwarning(
                "Kein QR-Code",
                "Bitte zuerst einen QR-Code erzeugen."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Dateien", "*.png"),
                ("JPEG Dateien", "*.jpg"),
                ("Alle Dateien", "*.*")
            ],
            title="QR-Code speichern"
        )

        if not file_path:
            return

        try:
            self.qr_image.save(file_path)
            self.status_var.set(f"Gespeichert: {os.path.basename(file_path)}")
            messagebox.showinfo(
                "Erfolgreich gespeichert",
                f"QR-Code wurde gespeichert:\n\n{file_path}"
            )

        except Exception as e:
            messagebox.showerror(
                "Speicherfehler",
                f"Datei konnte nicht gespeichert werden:\n\n{e}"
            )


def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
