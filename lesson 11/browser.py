class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f'Visiting {url}')

    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            prev_page = self.back_stack[-1]
            print(f'Go back: {prev_page}')
        else:
            print('Can not go back!')

    def forward(self):
        if self.forward_stack:
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f'Go forward: {next_page}')
        else:
            print('Can not go forward!')

def info(bs):
    print(f'|___ Back stack: {bs.back_stack}')
    print(f'|___ Forward stack: {bs.forward_stack}')
    print()

browser = Browser()

browser.visit_page('https://www.google.com')
browser.visit_page('https://www.facebook.com')
browser.visit_page('https://www.youtube.com')
info(browser)

browser.back()
info(browser)

browser.back()
info(browser)

browser.forward()
info(browser)

browser.forward()
info(browser)

browser.forward()
info(browser)
