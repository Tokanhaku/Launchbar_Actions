-- LaunchBar Action Script

tell application "System Events"
	tell appearance preferences
		set dark mode to not dark mode
		set it_is_dark to dark mode
	end tell
end tell

if it_is_dark = true then
	tell application "System Events" to set picture of every desktop to "/Library/Desktop Pictures/Mojave Night.jpg"
	-- tell application "System Events" to set picture of every desktop to "/Library/Desktop Pictures/Catalina Night.jpg"

	do shell script "defaults write at.obdev.LaunchBar Theme at.obdev.LaunchBar.theme.Dark"
else
	tell application "System Events" to set picture of every desktop to "/Library/Desktop Pictures/Mojave.heic"
	-- tell application "System Events" to set picture of every desktop to "/Library/Desktop Pictures/Catalina.heic"

	do shell script "defaults write at.obdev.LaunchBar Theme at.obdev.LaunchBar.theme.Default"
end if