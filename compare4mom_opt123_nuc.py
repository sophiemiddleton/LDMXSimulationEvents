from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TLorentzVector
import math
data01 =readLHEF('FFopt1/unweighted_events.lhe')
data02 =readLHEF('FFopt2/unweighted_events.lhe')
data03 =readLHEF('FFopt3/unweighted_events.lhe')

electrons01=data01.getParticlesByIDs([9000002,-9000002])
electrons02=data02.getParticlesByIDs([9000002,-9000002])
electrons03=data03.getParticlesByIDs([9000002,-9000002])

c=TCanvas()
c.Divide(2,2)
hist_4mom_diff_opt1=TH1F("#Delta q^{2} in opt1", "Outgoing - Incoming Nucleus q^{2} opt1", 100,30275,30280)
hist_4mom_diff_opt2=TH1F("#Delta q^{2} in opt2", "Outgoing - Incoming Nucelus q^{2} opt2", 100,30275,30280)
hist_4mom_diff_opt3=TH1F("#Delta q^{2} in opt2", "Outgoing - Incoming Nucelus q^{2} opt3", 100,0,4.5)
hist_4momRatio=TH1F("q^{2} out opt1/opt2", "Ratio q^{2} of opt1/opt2 ", 100,30275,30280)

for e in electrons01:
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)

    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)

    q2 = (outgoing - incoming).M2()
    print(q2)
    hist_4mom_diff_opt1.Fill(q2)

for e in electrons02:
    incoming = TLorentzVector()
    outgoing = TLorentzVector()
    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)

    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
    q2 = (outgoing - incoming).M2()
    hist_4mom_diff_opt2.Fill(q2)

for e in electrons03:
    incoming = TLorentzVector()
    outgoing = TLorentzVector()
    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
    q2 = (outgoing - incoming).M2()
    sigma = 6.4e4
    hist_4mom_diff_opt3.Fill(q2)


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
c.cd(4)
hist_4mom_diff_opt3.GetXaxis().SetTitle("#Delta q^{2}")
hist_4mom_diff_opt3.Draw()
#hist_4momRatio.Draw()
c.SaveAs("compare4mom_nuc.png")
