# Read parameters
from AllHadronicSUSY.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
#dataSetName = parameters.value("dataset","file:/pnfs/desy.de/cms/tier2/store/mc/Phys14DR/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F452BBD7-BE76-E411-B1D7-002590DB928E.root")
dataSetName = parameters.value("dataset","/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/162/00000/12284DB9-4227-E511-A438-02163E013674.root")
global_tag = parameters.value("global_tag","PHYS14_25_V2::All")
lostlepton= parameters.value("lostlepton", True)
tagandprobe= parameters.value("tagandprobe", False)
applybaseline= parameters.value("applybaseline", False)
doZinv=parameters.value("doZinv", True)
gridcontrol=parameters.value("gridcontrol", False)
numevents=parameters.value("numevents",-1)
geninfo=parameters.value("geninfo",False)

print "***** SETUP ************************************"
print " dataSetName : "+dataSetName
print " global_tag : "+global_tag
print " storing lostlepton variables: "+str(lostlepton)
print " storing tag and probe variables: "+str(tagandprobe)
print " storing Zinv variables: "+str(doZinv)
print " Applying baseline selection filter: "+str(applybaseline)
print " Including gen-level information: "+str(geninfo)
print "************************************************"

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
process = cms.Process("RA2EventSelection")

## configure geometry & conditions
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
  outFileName="ReducedSelection",
  reportEveryEvt=1000,
  testFileName=dataSetName,
  Global_Tag=global_tag,
  numProcessedEvt=numevents,
  lostlepton=lostlepton,
  tagandprobe=tagandprobe,
  applybaseline=applybaseline,
  doZinv=doZinv,
  geninfo=geninfo
)

