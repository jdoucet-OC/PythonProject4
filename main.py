import controller
import views


def main():
    view = views.Views()
    start = controller.Controller(view)
    start.run()


if __name__ == "__main__":
    main()
