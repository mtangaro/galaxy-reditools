# galaxy-reditools

This is not a production code. Only for testing purpose!


# istructions

1. Add to galaxy/config/too_conf.xml

  <label id="reditoos" text="REDItools" />
  <section name="REDItools" id="reditools">
    <tool file="reditools/REDItoolDnaRna_wrapper.xml" />
  </section>

2. Clone the repository

  git clone https://github.com/mtangaro/galaxy-reditools.git reditools
  
3. Move reditools dir in galaxy/tools/

4. restart galaxy
