class Settings:
	"""A class to store all settings for Alein Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5

		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255,0,0)
		self.bullets_allowed = 3


		# Alien settings.
		# alien_frequncy controls how often a new alien appear.s
		# Higher values -> more frequent aliens. Max = 1.0.
		self.alien_frequency = 0.008
		self.alien_speed = 1.5