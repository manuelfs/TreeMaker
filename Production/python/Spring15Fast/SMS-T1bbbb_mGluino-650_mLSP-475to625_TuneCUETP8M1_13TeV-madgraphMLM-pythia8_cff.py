import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/065A6B24-9066-E511-A38C-002590AC4C7C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/08960452-9066-E511-B858-002590491AE4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/12001497-9066-E511-AA26-0CC47A13CB18.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/1418B92D-9066-E511-8F1D-003048F5B2B4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/18246666-9066-E511-8954-003048344B08.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/24483729-9066-E511-9E23-0025907FD2BA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/28D23367-9066-E511-BD5A-0025907253E0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/2E038E26-9066-E511-B66D-0025908217DA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/2E43142E-9066-E511-817A-0025907DC9F8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/301A172A-9066-E511-8F86-0025907DC9F2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/34D5E3F8-8F66-E511-894E-0CC47A13CDB0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/38413D25-9066-E511-B337-047D7B881D62.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/3846F44A-9066-E511-B536-0CC47A13D110.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/404F0F00-9166-E511-8989-003048341AFA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/420F8E8D-9066-E511-9E66-00259084A6C4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/4E987E16-9166-E511-AF61-003048344A94.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/52C5C652-9066-E511-9F35-003048F5B2A0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/5601FC23-9066-E511-BD16-002590AC4C7C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/5E61FD5F-9066-E511-B072-0025904A9430.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/60F19E2C-9066-E511-A86C-047D7B881D3A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/62E85D29-9066-E511-B001-0025907FD2BA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/6E1D2328-9066-E511-924C-003048F5B69C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/6E225E4C-9066-E511-8EFA-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/76835528-9066-E511-9094-047D7B881D1E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7ABCD524-9066-E511-ABC2-047D7BD6DDAC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7CBE0429-9066-E511-A58F-90B11C267182.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/849EB101-9166-E511-8DC9-002590488694.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/8CB6F515-9166-E511-9D16-003048F5B2B4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/9222EC2B-9066-E511-8885-047D7B881D76.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/9A8AA7FA-9066-E511-9A5D-002590E2DA08.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/A49AB73A-9066-E511-AB22-90B11C27EA38.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/A6D89729-9066-E511-9B8C-047D7BD6DEF2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/B0ACD8A0-9066-E511-BFEB-0025901D0946.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/B646C97E-9066-E511-A4EA-002590EFF972.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/BC2E402E-9066-E511-943C-0025907DC9BE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/BC56A02D-9066-E511-882D-0025907DC9F8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/D6388623-9066-E511-97C6-047D7BD6DDA6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/DC59EB50-9066-E511-8CA0-003048F5B5F4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E0FDEC8D-9066-E511-AD6A-003048F5ADF2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E4D0E24D-9066-E511-BFB3-003048F5B69C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E8114B23-9066-E511-9D00-047D7BD6DDA6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E855F58E-9066-E511-84EA-003048F59728.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E8FE1A66-9066-E511-86B5-0025904AC2C4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/EE259302-9066-E511-83D0-003048F5B69C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/EE845928-9066-E511-A518-047D7B881D1E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/EEB76025-9066-E511-A396-047D7B881D62.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F2624028-9066-E511-AE66-047D7B881D1E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F87BC72C-9066-E511-99C4-047D7B881D3A.root' ] );


secFiles.extend( [
               ] )

