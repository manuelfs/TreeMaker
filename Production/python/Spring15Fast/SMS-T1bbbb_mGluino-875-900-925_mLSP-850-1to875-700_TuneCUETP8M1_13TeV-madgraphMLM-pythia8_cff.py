import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/00DFC56E-F95B-E511-B21D-782BCB407CF7.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/0E79C869-F95B-E511-8115-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/10048B7E-F95B-E511-A53D-0025901D0C68.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/103A7F72-F95B-E511-BD41-000F530E4794.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/14A0FC71-F95B-E511-BC9F-0025904AC2C6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/1679E166-F95B-E511-90AC-001E675A58D9.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/1AE82451-F95B-E511-81AD-001517E73B50.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/38E65775-F95B-E511-B076-782BCB286045.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/40B1746C-F95B-E511-9E33-0CC47A13D2BE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/42B74D68-F95B-E511-9E81-001E67A4069F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/42F70066-F95B-E511-B115-0CC47A6B5B20.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/4C49DB75-F95B-E511-A65E-842B2B2B0DAD.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/508C8D6D-F95B-E511-9B74-00259048BF92.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/58B0D56C-F95B-E511-A354-002590E39D8A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/5A0F4A6A-F95B-E511-B5BD-0CC47A13D052.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/5C836678-F95B-E511-89F3-0025901D0C52.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/5EBBF478-F95B-E511-82D9-001E675A6D10.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/7CECE56A-F95B-E511-A846-0CC47A13CD44.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/82828868-F95B-E511-AB22-0CC47A13CDA0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/86C6E76B-F95B-E511-818F-002590E3A024.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/88769868-F95B-E511-BC4F-0CC47A13D110.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/8E79326B-F95B-E511-80BF-002590E3A2D6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/94FD6C6A-F95B-E511-A68C-002590E2F664.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/98704872-F95B-E511-A8BF-842B2B182385.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/9A915E6B-F95B-E511-9BE7-002590E2DD10.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/9C495169-F95B-E511-B310-0CC47A13D0F2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/ACEF3C86-F95B-E511-A1AC-00259048B754.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/B0F4D070-F95B-E511-A79A-001E675A6725.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/B251816B-F95B-E511-B453-90B11C06954E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/BE918679-F95B-E511-AFCC-842B2B185476.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/C08DCA6E-F95B-E511-A80C-001517F7F524.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/C0A13B76-F95B-E511-9285-001517E7410C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/C48B8D6D-F95B-E511-A237-00259048BF92.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/D02E8968-F95B-E511-9008-0026181D28BB.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/E046757C-F95B-E511-AD17-0025901D16B0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/E0BB306A-F95B-E511-99D6-F45214C748C2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/E2C0656F-F95B-E511-9C06-002590491B1E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/E8AA6868-F95B-E511-8844-0026181D28BB.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/F061B084-F95B-E511-AD0A-001517E736AC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/F0B7666E-F95B-E511-A9E6-90B11C27EA38.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/F24EEE75-F95B-E511-B43F-842B2B2A9926.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/F85E5D73-F95B-E511-8721-0025904886E6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/FCE05176-F95B-E511-9B83-000F530E46D8.root' ] );


secFiles.extend( [
               ] )

