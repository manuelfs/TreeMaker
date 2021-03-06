import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/0E389F4D-7142-E511-ADD7-842B2B019EA1.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/12932C9C-A541-E511-B993-001517FB25E4.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/1E4E1D32-A841-E511-835C-002354EF3BCE.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/4A159436-A841-E511-A395-003048FF9AA6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/52180E15-5842-E511-8866-0015C5F82CF4.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/52C7E836-A841-E511-9714-00259059642A.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/5A71E170-9B41-E511-9D21-0025905C3E66.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/64375477-7442-E511-858A-0025905C2CA6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/6C8025D9-AF41-E511-B76D-0025905A6134.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/7432BB76-9A41-E511-9738-0025905C3E66.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/8A36C37E-7442-E511-86C5-008CFA197968.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/A601D872-9941-E511-A239-0025905C3E66.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/B2AE83D8-A641-E511-A395-90B11C043098.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/B84C2E95-A541-E511-A3F8-90B11C043098.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/BE48C914-7442-E511-BBDD-0025905A607E.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/BE63E7AE-A641-E511-B8A4-90B11C050429.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/C6ADD393-B541-E511-98E2-008CFA197968.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/CAEF887E-7442-E511-8433-001517E73B50.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/E48EE664-6842-E511-B8B0-C4346BC87798.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/06C9E488-1747-E511-BBEB-002590207C28.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/0A8D6336-5B41-E511-B0CE-00266CFFBF84.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/0E0014E4-5841-E511-84F6-B083FED40671.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/262308FA-5941-E511-A929-0025905C3E68.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/3449ADFC-3B42-E511-9FA2-0025904C4E2A.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/3A7953A6-3D42-E511-B96E-B083FED024B2.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/40FBA99E-5841-E511-B9FB-D4AE5265ABA5.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/423E8811-3542-E511-BFA0-D4AE526A0D22.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/467A95DF-5B41-E511-848F-B083FED429D6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/48EC23DF-5941-E511-A4BD-0025905C3E68.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/5807C68E-4042-E511-9F8F-C4346BC8D390.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/640F0CA0-5841-E511-92B5-B083FECF83AB.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/720B18E4-5841-E511-B065-782BCB53A3A6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/74044DEB-5841-E511-8574-B083FED42FE4.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/768AC1DE-5941-E511-B163-0025905C3E66.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/9C66EC98-1747-E511-BD88-0021284004A6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/B087A307-4442-E511-82E1-02163E014236.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/CA89980B-7141-E511-8E33-002618943979.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/EAF6218F-1747-E511-A99B-842B2B185C54.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/106FC3C3-DB40-E511-9298-0026189438E6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/16E1D0B6-DB40-E511-88BC-0025905C43EC.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/787C55C6-DB40-E511-AF5D-003048FFCC1E.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/8CD0CE76-DB40-E511-B849-0002C90F8088.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B2FF8748-DD40-E511-B5AE-E0DB55FC1055.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/06E14A2E-0E41-E511-97E6-0026189438B4.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/08677543-0F41-E511-A17B-002590D60004.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0C9B329E-0A41-E511-85FF-00266CFFC43C.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/10A8EC23-F541-E511-9EF7-0025904B7C24.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/26F8DB3C-0F41-E511-8645-0025904CF758.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3209D962-1041-E511-A31C-0025905938A4.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4E2427C1-2241-E511-85D9-02163E014797.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/52CDE691-0D41-E511-A0F3-0025905A48BC.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/60C86833-0E41-E511-A158-0025905A48D6.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6EB9B9E5-1041-E511-9A98-002590D6004A.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/72C34DAC-E341-E511-9CD1-6CC2173BBEE0.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8018FAC2-2241-E511-BBC0-02163E01463E.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/822EDC5D-1041-E511-978A-0025904CF758.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/826A7474-ED41-E511-B5C8-0025905AA9CC.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/82773C8F-0D41-E511-9B7C-0025905B85AA.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/86DF6771-ED41-E511-94CD-0025905A4964.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8CB6848F-0D41-E511-B070-0025905A48B2.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9019BD1B-2341-E511-8CC2-02163E0133AC.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/949EC787-6446-E511-AB27-B083FED04276.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/96D59290-1141-E511-80A4-0025905C4300.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/98134330-0E41-E511-B9D1-00261894398A.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B4DE54EE-5141-E511-A53F-0025905C975E.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B6292171-5141-E511-82E5-0025905C94D2.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B8E33B3C-0F41-E511-95B8-0025904CF100.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D86EA076-5A42-E511-9D63-02163E0141E4.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DCDBF751-F841-E511-B2F6-002590A81EF0.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DE98FC92-0D41-E511-9831-0025905B855E.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E2F4DE4F-E041-E511-BB71-002590D60150.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E83873B9-1141-E511-A85D-0025904CF758.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC91815D-1041-E511-A1E7-0025905C4300.root',
       '/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FCD4E22E-0E41-E511-80AB-0025905A60F8.root' ] );


secFiles.extend( [
               ] )

