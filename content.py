# -*- coding: utf-8 -*-


def head():
    head = """
    <head>
        <meta charset="utf-8">
        <link href="style" rel="stylesheet">
    </head>"""
    return head


def menu():
    menu = """
        <div class="menu_box">
            <a href="index"><div class="Menu">Главная</div></a>
            <a href="about"><div class="Menu">Обо мне</div></a>
            <a href="science"><div class="Menu">Наука</div></a>
            <a href="contacts"><div class="Menu">Контакты</div></a>
        </div>"""
    return menu


def footer():
    footer = """
    <footer class="footer">
        <p>
            Lastockkina Maria<br>
            Copyright &copy; 2017
        </p>
    </footer> <!-- .footer -->"""
    return footer


def html_all(menu, content, right_sidebar):
    html = ("""
        <html>"""
            + head() +
            """<body>
                <a href="#top"><div class="up"></div></a>
                <div class="wrapper">
                    <header class="header" name="top">
                        <div class="head_block">
                            <div class="logo">
                            </div>"""
                            + menu +
                        """</div>
                    </header> <!-- .header-->
                    <div class="middle">
                        <div class="container">"""
                         + content +
                        """</div><!-- .container-->
                        <div class="right-sidebar">"""
                        + right_sidebar +
                        """</div>
                    </div><!-- .middle-->"""
                    + footer() +
                """</div><!-- .wrapper -->
            </body>
        </html>""")
    return html


if __name__ == '__main__':
    print('Это модуль, содержащий html-шаблон сайта')
    input('Для продолэения введите любой символ...')