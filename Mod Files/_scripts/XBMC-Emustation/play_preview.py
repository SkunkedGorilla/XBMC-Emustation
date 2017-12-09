import glob, os, xbmc, time
## Play preview video if it exists
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Preview_Path)' ) ) == "1":
	Previews_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Preview_Path)' )
else:
	Previews_Path		= "Q:\\" + '_previews\\'

if xbmc.getInfoLabel('Skin.String(emuname)') == "xbox" or xbmc.getInfoLabel('Skin.String(emuname)') == "ports":
	Focus		= "50"
	Path		= xbmc.getInfoLabel('listitem.path')
	if xbmc.getCondVisibility( 'Skin.HasSetting(resourcesvideo)' ): Path = os.path.join( Path, '_resources\\media\\')
	FileName	= "Preview"
else:
	Focus		= "9000"
	Path		= os.path.join( Previews_Path, xbmc.getInfoLabel('Skin.String(emuname)') )
	FileName	= xbmc.getInfoLabel('Container(9000).ListItem.Label')

if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
	VideoFile = ""
	if xbmc.Player().isPlayingVideo():
		xbmc.Player().stop()
		xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
	else:
		for Files in glob.glob( os.path.join( Path, FileName + ".*") ):
			VideoFile = Files
		if os.path.isfile( VideoFile ):
			if VideoFile.endswith("xmv") or VideoFile.endswith("mp4"):
				print "dvdplayer"
				player = xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER )
			else:
				print "mplayer"
				player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
			xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
			time.sleep(1)
			xbmc.executebuiltin( 'SetFocus(9100)' )
		else:
			xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
else:
	xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )