from pygame import *

DEFAULT_TEXT = {"text": "DefaultText", "font": None, "size": 16}

class Button:
  def __init__(
    self, 
    supersurf,
    position,
    size,
    on_click,
    on_click_args,  # dictionary
    color={'foreground': (0, 0, 0), 'background': None},
    text=DEFAULT_TEXT,
    border_width=1,
    border_radius=[-1, -1, -1, -1],
  ):
    self.surface = Surface(size)
    self.surface.fill((255, 255, 255) if not color['background'] else color['background'])
    self.position = position
    self.size = size
    self.super_surf = supersurf
    self.color = color
    self.label = Label(self.surface, (size[0]//2, size[1]//2), text['size'], color['background'], color['foreground'], text['font'], text['text'])
    self.border_width = border_width
    self.border_rad = border_radius
    self.click_event = on_click
    self.click_args = on_click_args
    
    self.tmp = False
  
  def draw(self):
    draw.rect(
      self.surface, 
      self.color['foreground'], 
      [0, 0, self.size[0], self.size[1]], 
      width=self.border_width,
      border_top_left_radius=self.border_rad[0],
      border_top_right_radius=self.border_rad[1],
      border_bottom_left_radius=self.border_rad[2],
      border_bottom_right_radius=self.border_rad[3]
    )
    self.label.draw()
    self.super_surf.blit(self.surface, self.position)
  
  def event_check(self, events):
    if not events:
      return
    mpos = mouse.get_pos()
    for event in events:
      # apply match case
      if event.type == MOUSEBUTTONDOWN:
        if self.position[0] <= mpos[0] <= self.position[0]+self.size[0]:
          if self.position[1] <= mpos[1] <= self.position[1]+self.size[1]:
            self.tmp = True
      if event.type == MOUSEBUTTONUP:
        if self.position[0] <= mpos[0] <= self.position[0]+self.size[0]:
          if self.position[1] <= mpos[1] <= self.position[1]+self.size[1]:
            if self.tmp:
              self.click_event(self.click_args)


class Label:
  def __init__(
    self,
    supersurf,
    position,
    size,
    back_color,
    color,
    font_name=None,
    text="DefaultText"
  ):
    self.super_surf = supersurf
    self.font = font.SysFont(font_name, size, False, False)
    self.position = position
    self.color = color
    self.back_color = back_color
    self.text_set(text)

  def text_set(self, text):
    self.surface = self.font.render(text, True, self.color, self.back_color)

  def draw(self):
    self.super_surf.blit(self.surface, self.surface.get_rect(center=self.position))