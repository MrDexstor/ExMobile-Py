from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
import mysql.connector

ex_projects = mysql.connector.connect(
    host="51.83.165.198",
    user="mrdexstor",
    password="admin_ex",
    database="ex_base")

KV = '''
MDScreen:
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'База пользователей'
            icon: 'account-box-multiple-outline'
            MDScreen:
                MDScrollView:
                    MDList:
                        id: container
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'База пользовxdfnhателей'
            icon: 'account-box-multiple-outline'
'''


class ExMobile(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        base = ex_projects.cursor()
        g = 1
        for i in range(64):
            base.execute("SELECT name FROM dlu_users WHERE user_id = %s", (g,))

            lines = base.fetchone()
            g = g + 1
            if lines is not None:
                line = lines[0]
            else:
                continue

            self.root.ids.container.add_widget(
                OneLineListItem(text=f"{line} ({g})")
            )
        print(g)


ExMobile().run()
