# ray test added
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# ray: user added => signals.py receiver => consumers.py user_gossip => home.html webSocketBridge.listen

# ray: receives when a user is added, this is the way to webSocketBridge.listen in home.html
@receiver(post_save, sender=User)
def announce_new_user(sender, instance, created, **kwargs):  # ray: name of following method is arbitrary
    if created:
        channel_layer = get_channel_layer()
        # ray: send message to group
        print("ray : ----- signals.py receiver announce_new_user -----")
        async_to_sync(channel_layer.group_send) (
            "gossip", { # ray: this is event parameter in await 'self.send_json(event)' of consumers.py
                "type": "user.gossip",  # ray: type name corresponds to user_gossip in signals.py
                "event": "New User",
                "username": instance.username # ray: added username
            }
        )
