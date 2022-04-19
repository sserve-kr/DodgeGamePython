from pygame import *

DEFAULT_TEXT = {"text": "DefaultText", "font": None, "size": 16, "bold": False, "italic": False, "antialiase": True}

class Button:
  def __init__(
    self, 
    supersurf, 
    position, 
    size,
    color={'foreground': (0, 0, 0), 'background': None},
    text=DEFAULT_TEXT
    border={'width': 0, 'radius': [-1, -1, -1, -1]},
    on_click=callback
  ):
    self.surface = Surface(size)
    self.position = position
    self.size = size
    self.super_surf = supersurf
    self.color = color
    self.font = font(text["font"], text["size"], text["bold"], text["italic"])
    self.text_change(text)
    self.border_width = border['width']
    self.border_rad = border['radius']
    self.click_event = on_click
    
    self.tmp = False
  
  def draw(self):
    draw.rect(
      self.surface, 
      self.color, 
      [0, 0, size[0], size[1]], 
      width=self.border_width,
      border_top_left_radius=self.border_rad[0],
      border_top_right_radius=self.border_rad[1],
      border_bottom_left_radius=self.border_rad[2],
      border_bottom_right_radius=self.border_rad[3]
    )
    self.surface.blit(self.text, self.text.get_rect())
    self.super_surf.blit(self.surface, self.position)
  
  def text_change(self, text=DEFAULT_TEXT):
    self.text = self.font.render(text["text"], text["antialiase"], self.color['foreground'], background=self.color['background'])
    temp_rect = self.text.get_rect()
    temp_rect.centerx = self.size[0]//2
    temp_rect.centery = self.size[1]//2
  
  def event_check(self, events):
    if not events:
      return
    mpos = mouse.get_pos()
    for event in events:
      match event.type:
        case MOUSEBUTTONDOWN:
          if self.position[0] <= mpos[0] <= self.position[0]+self.size[0]:
            if self.position[1] <= mpos[1] <= self.position[1]+self.size[1]:
              tmp = True
        case MOUSEBUTTONUP:
          if self.position[0] <= mpos[0] <= self.position[0]+self.size[0]:
            if self.position[1] <= mpos[1] <= self.position[1]+self.size[1]:
              if tmp:
                self.click_event()