
class CrosshairRenderer:
    def __init__(self, canvas, crosshair, crosshair_manager):
        self.canvas = canvas
        self.crosshair = crosshair
        self.crosshair_manager = crosshair_manager
        self.update_screen_size()
        self.draw_crosshair()
        

    def draw_crosshair(self):
        self.update_screen_size()
        self.canvas.delete("all")

        color = '#90EE90'
        width = self.crosshair.width
        line_size = self.crosshair.length
        gap = self.crosshair.gap

        x_center = self.screen_size[0] // 2
        y_center = self.screen_size[1] // 2

        self.up_line = self.canvas.create_line(x_center, y_center-gap, x_center, y_center-gap-line_size, fill=color, width=width)
        self.down_line = self.canvas.create_line(x_center, y_center+gap, x_center, y_center+gap+line_size, fill=color, width=width)
        self.left_line = self.canvas.create_line(x_center-gap, y_center, x_center-gap-line_size, y_center, fill=color, width=width)
        self.right_line = self.canvas.create_line(x_center+gap, y_center, x_center+gap+line_size, y_center, fill=color, width=width)

        dot = self.crosshair.get_dot()
        if dot.is_it_dot():
            r = dot.dot_size
            self.crosshair_dot = self.canvas.create_oval(x_center-r, y_center-r, x_center+r, y_center+r, fill=color, outline="")

        self.crosshair.save_to_json(self.crosshair_manager.get_data_manager().get_last_crosshair_path())


    def update_crosshair(self, attribute, value):
        self.update_screen_size()
        if "dot" in attribute:
            dot = self.crosshair.get_dot()
            setattr(dot, attribute, value)
            self.crosshair.set_dot(dot)
        else:
            setattr(self.crosshair, attribute, value)
        
        self.draw_crosshair()


    def update_screen_size(self):
        self.screen_size = self.crosshair_manager.get_screen_size()