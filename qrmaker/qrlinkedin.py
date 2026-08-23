import qrcode

linkedin = qrcode.make("https://beta.clous.app/labs/showclous")
linkedin.save("Take_Clous_Tour.webp", format="WEBP")
