from direct.showbase.ShowBase import ShowBase
from planetSim.Planet import Planet

earth = Planet(1004, 1242, [0, 0])


class Simulation(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)


app = Simulation()
app.run()
