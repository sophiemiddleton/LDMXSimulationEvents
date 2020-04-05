from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data02 =readLHEF('FFopt1/unweighted_events.lhe')
data03 =readLHEF('FFopt2/unweighted_events.lhe')

electrons02=data02.getParticlesByIDs([11,-11])
electrons03=data03.getParticlesByIDs([11,-11])

c=TCanvas()
c.Divide(1,3)
hist_4mom_diff_opt1=TH1F("#Delta q^{2} in opt1", "Outgoing - Incoming Electron q^{2} opt1", 100,0,100)
hist_4mom_diff_opt2=TH1F("#Delta q^{2} in opt2", "Outgoing - Incoming Electron q^{2} opt2", 100,0,100)
hist_4momRatio=TH1F("q^{2} out opt1/opt2", "Ratio q^{2} ", 100,0,100)

for e in electrons02:
    squared_4mom_in = 0
    squared_4mom_out = 0
    if e.status is -1 :
        print('incoming', e.eventid)
        squared_4mom_in = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
    if e.status is 1:
        print('outgoing', e.eventid)
        squared_4mom_out = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
    hist_4mom_diff_opt1.Fill(squared_4mom_out-squared_4mom_in)

for e in electrons03:
    squared_4mom_in = 0
    squared_4mom_out = 0
    if e.status is -1 :
        print('incoming', e.eventid)
        squared_4mom_in = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
    if e.status is 1:
        print('outgoing', e.eventid)
        squared_4mom_out = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
    hist_4mom_diff_opt2.Fill(squared_4mom_out-squared_4mom_in)


c.cd(1)
hist_4mom_diff_opt1.GetXaxis().SetTitle("#Delta q^{2}")
hist_4mom_diff_opt1.Draw()
c.cd(2)
hist_4mom_diff_opt2.GetXaxis().SetTitle("#Delta q^{2}")
hist_4mom_diff_opt2.Draw()
for i in range(0,hist_4mom_diff_opt2.GetNbinsX()):
    if hist_4mom_diff_opt2.GetBinContent(i) !=0 :
        ratio = hist_4mom_diff_opt1.GetBinContent(i)/hist_4mom_diff_opt2.GetBinContent(i)
        hist_4momRatio.SetBinContent(i,ratio)
c.cd(3)
hist_4momRatio.Draw()
#hist_4momRatio.Draw()
c.SaveAs("compare4mom.png")
