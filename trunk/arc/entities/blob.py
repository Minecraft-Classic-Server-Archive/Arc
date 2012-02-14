# Arc is copyright 2009-2012 the Arc team and other contributors.
# Arc is licensed under the BSD 2-Clause modified License.
# To view more details, please see the "LICENSING" file in the "docs" folder of the Arc Package.

var_cango = True
try:
    blocktocheck = ord(world.blockstore.raw_blocks[world.blockstore.get_offset(x, y - 1, z)])
    if blocktocheck != 0:
        var_cango = False
except:
    var_cango = False
if var_cango:
    block = '\x00'
    world[x, y, z] = block
    self.client.queueTask(TASK_BLOCKSET, (x, y, z, block), world=world)
    self.client.sendBlock(x, y, z, block)
    var_position = (x, y - 1, z)
    x, y, z = var_position
    block = chr(11)
    world[x, y, z] = block
    self.client.queueTask(TASK_BLOCKSET, (x, y, z, block), world=world)
    self.client.sendBlock(x, y, z, block)
else:
    closestposition = (0, 0)
    closestclient = None
    closestdistance = None
    for entry in userpositionlist:
        client = entry[0]
        var_pos = entry[1]
        i, j, k = var_pos
        distance = ((i - x) ** 2 + (j - y) ** 2 + (k - z) ** 2) ** 0.5
        if closestdistance == None:
            closestdistance = distance
            closestclient = client
            closestposition = (var_pos[0], var_pos[2])
        else:
            if distance < closestdistance:
                closestdistance = distance
                closestclient = client
                closestposition = (var_pos[0], var_pos[2])
    if closestdistance < 2:
        sx, sy, sz, sh = world.spawn
        closestclient.teleportTo(sx, sy, sz, sh)
        self.client.sendWorldMessage("%s has died from a blob." % closestclient.username)
    if closestdistance != 0:
        i, k = closestposition
        target = [int((i - x) / (closestdistance / 1.75)) + x, y, int((k - z) / (closestdistance / 1.75)) + z]
        i, j, k = target
        var_cango = True
        try:
            blocktocheck = ord(world.blockstore.raw_blocks[world.blockstore.get_offset(i, j, k)])
            if blocktocheck != 0:
                var_cango = False
        except:
            var_cango = False
        if var_cango:
            block = '\x00'
            world[x, y, z] = block
            self.client.queueTask(TASK_BLOCKSET, (x, y, z, block), world=world)
            self.client.sendBlock(x, y, z, block)
            var_position = target
            x, y, z = var_position
            block = chr(11)
            world[x, y, z] = block
            self.client.queueTask(TASK_BLOCKSET, (x, y, z, block), world=world)
            self.client.sendBlock(x, y, z, block)
        else:
            var_cango = True
            target[1] = target[1] + 1
            j = target[1]
            try:
                blocktocheck = ord(world.blockstore.raw_blocks[world.blockstore.get_offset(i, j, k)])
                if blocktocheck != 0:
                    var_cango = False
            except:
                var_cango = False
            if var_cango:
                block = '\x00'
                world[x, y, z] = block
                self.client.queueTask(TASK_BLOCKSET, (x, y, z, block), world=world)
                self.client.sendBlock(x, y, z, block)
                var_position = target
                x, y, z = var_position
                block = chr(11)
                world[x, y, z] = block
                self.client.queueTask(TASK_BLOCKSET, (x, y, z, block), world=world)
                self.client.sendBlock(x, y, z, block)
