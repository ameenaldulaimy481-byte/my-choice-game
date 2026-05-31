import flet as ft
from datetime import datetime, timedelta

def main(page: ft.Page):
    page.title = "دعوة زفاف"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#FDFBF7" # لون كريمي هادئ

    # حساب التاريخ بعد أسبوع
    wedding_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    def show_invite(e):
        circle_container.visible = False
        invite_card.visible = True
        page.update()

    # الدائرة (البوتن)
    circle_container = ft.Container(
        content=ft.FilledButton(
            content=ft.Text("اضغط لفتح الدعوة", size=20, weight="bold"),
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=40),
            on_click=show_invite,
            bgcolor="#C5A059" # لون ذهبي
        ),
        width=250, height=250,
        alignment=ft.alignment.center,
    )

    # كارت الدعوة المرتب
    invite_card = ft.Container(
        content=ft.Column([
            ft.Text("دعوة زفاف", size=32, weight="bold", color="#8B7355"),
            ft.Divider(),
            ft.Text("يتشرف زينب وعبدالله بدعوتكم لحفل زفافهم السعيد", size=20, text_align="center"),
            ft.Container(height=20),
            ft.Text(f"التاريخ: {wedding_date}", size=18, weight="bold"),
            ft.Text("الموقع: بغداد - العامرية", size=18),
            ft.Container(height=30),
            ft.Text("تنورونا وتشرفونا!", size=22, weight="bold", color="#8B7355"),
            ft.Container(height=20),
            ft.Text("ملاحظة: نعتذر عن استقبال فاطمة في الحفل", size=14, color="red", italic=True),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=40,
        border=ft.border.all(2, "#C5A059"),
        border_radius=20,
        visible=False,
        width=400,
    )

    page.add(circle_container, invite_card)

ft.app(target=main)
