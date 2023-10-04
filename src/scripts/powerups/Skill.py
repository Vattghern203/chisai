from typing import Literal

class Skill:

    def __init__(
            self,
            name: str,
            cooldown: int,
            duration: float | int,
            effect: function,
            target: Literal["self", "enemy", "ally"] = "self",

        ) -> None:

        self.name = name
        self.cooldown = cooldown
        self.duration = duration
        self.effect = effect
        self.target = target

        self.cooldown_counter: int = 0
        self.on_cooldown: bool = False


    def activate_skill(self) -> None:

        if not self.on_cooldown:

            self.effect()

            self.on_cooldown = True


    def handle_cooldown(self) -> None:

        if self.on_cooldown and self.cooldown_counter < self.cooldown:

            self.cooldown_counter += 1

        else:

            self.on_cooldown = False      