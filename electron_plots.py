from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data=readLHEF('unweighted_events.lhe')
electrons=data.getParticlesByIDs([11,-11])
c=TCanvas()
c.Divide(2,2)
hist_e_theta=TH1F("theta_elec", "Outgoing Electron Theta",100,-1,1)
hist_4in=TH1F("q^{2} in", "Incoming Electron q^{2} ", 100,0,100)
hist_4out=TH1F("q^{2} out", "Outgoing Electron q^{2} ", 100,0,100)
hist_4momRatio=TH1F("q^{2} out", "Ratio q^{2} ", 100,0,100)
for e in electrons:

    if e.status is -1 :
        squared_4mom = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)
    if e.status is 1:
        val = math.atan(e.py/e.pz)
        hist_e_theta.Fill(val)
        squared_4mom = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
        hist_4out.Fill(squared_4mom)


c.cd(1)
hist_e_theta.GetXaxis().SetTitle("#theta")
hist_e_theta.Draw()
c.cd(2)
hist_4in.GetXaxis().SetTitle("q^{2}_{e_{in}}")
hist_4in.Draw()
c.cd(3)
hist_4out.GetXaxis().SetTitle("q^{2}_{e_{out}}")
hist_4out.Draw()
c.SaveAs("electron_plots.png")
