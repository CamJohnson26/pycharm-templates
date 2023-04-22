from cmd import Cmd


class CLIApp(Cmd):
    prompt = '>>> '

    def do_greet(self, args):
        first_name, last_name = args.rsplit(" ", 1)
        print(f"Hello, {last_name}, {first_name}!")

    def do_exit(self, args):
        raise SystemExit()


if __name__ == '__main__':
    CLIApp().cmdloop("Enter a command (greet, exit):")
