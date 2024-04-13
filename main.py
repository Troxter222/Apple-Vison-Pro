# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.graphics.texture import Texture
# from kivy.clock import Clock
# from kivy.core.window import Window

# import cv2

# class CameraApp(App):
#     def build(self):
#         Window.fullscreen = 'auto'

#         self.img = Image(size=Window.size, allow_stretch=True)

#         self.capture = cv2.VideoCapture(0)
#         if not self.capture.isOpened():
#             print("Could not open webcam")
#             exit()

#         Clock.schedule_interval(self.update, 1.0 / 30.0)

#         return self.img

#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             frame = cv2.flip(frame, 1)

#             buffer = cv2.flip(frame, 0).tostring()
#             texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
#             self.img.texture = texture

#     def on_stop(self):
#         self.capture.release()

# if __name__ == '__main__':
#     CameraApp().run()


import cv2
import kivy

print(kivy.__version__)
print(cv2.__version__)
