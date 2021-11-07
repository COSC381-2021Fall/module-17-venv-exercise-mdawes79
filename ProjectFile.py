import emoji
import pyjokes
import numpy

print(emoji.emojize("Python can be :beaming_face_with_smiling_eyes:"))
print(emoji.emojize("Computer science classes can be :unamused_face:"))

print(pyjokes.get_joke())

print(numpy.sin(numpy.pi/2.))
print(numpy.sin(numpy.array((0., 30., 45., 60., 90.)) * numpy.pi / 180. ))