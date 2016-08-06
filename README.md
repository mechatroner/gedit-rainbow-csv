# gtk_gedit_rainbow_csv
syntax highlighting rules for *.csv files in gtk (gedit)


##Installation Instructions:

Place csv.lang in your gtksourceview-2.0/language-specs directory
and make sure that it is readable for the user(s).

You must have root access to access to place it into 
`/usr/share/gtksourceview-2.0/language-specs/`
but as a regular user you can also put it under 
`~/.gnome2/gtksourceview-2.0/language-specs/`

The syntax definition contains some styles that are not present in
the default style definitions. Therefore you must add the following lines
to every xml style file in /usr/share/gtksourceview-2.0/styles/
in the `<style-scheme>` section:

```
<style name="csv:red"             foreground="#FF0000" bold="true"/>
<style name="csv:blue"            foreground="#0000FF" bold="true"/>
<style name="csv:green"           foreground="#00A000" bold="true"/>
<style name="csv:magenta"         foreground="#FF00FF" bold="true"/>
<style name="csv:brown"           foreground="#964B00" bold="true"/>
<style name="csv:dark_red"        foreground="#FF0000" bold="false"/>
<style name="csv:dark_blue"       foreground="#0000FF" bold="false"/>
<style name="csv:dark_green"      foreground="#009000" bold="false"/>
<style name="csv:dark_magenta"    foreground="#FF00FF" bold="false"/>
```

(look for "Language specific styles")
You may want to adjust the colors according to your style template.
If you don't have root access copy the xml files to
`~/.gnome2/gtksourceview-2.0/styles/`
and edit them there. Then you must probably go to 
Edit > Preferences > Font & colors to add the correct Color Schemes
