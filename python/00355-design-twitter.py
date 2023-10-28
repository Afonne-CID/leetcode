def follow(self, followerId: int, followeeId: int) -> None:
    self.followMap[followerId].add(followeeId)

def unfollow(self, followerId: int, followeeId: int) -> None:
    # Ensure a user does not unfollow themself
    if followerId != followeeId:
        self.followMap[followerId].discard(followeeId)
