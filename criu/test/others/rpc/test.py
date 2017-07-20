#!/usr/bin/python2

import socket, os, imp, sys
import rpc_pb2 as rpc
import argparse

parser = argparse.ArgumentParser(description="Test dump/restore using CRIU RPC")
parser.add_argument('socket', type = str, help = "CRIU service socket")
parser.add_argument('dir', type = str, help = "Directory where CRIU images should be placed")

args = vars(parser.parse_args())

# Connect to service socket
s = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)
s.connect(args['socket'])

# Create criu msg, set it's type to dump request
# and set dump options. Checkout more options in protobuf/rpc.proto
req			= rpc.criu_req()
req.type		= rpc.DUMP
req.opts.leave_running	= True
req.opts.log_level	= 4
req.opts.images_dir_fd	= os.open(args['dir'], os.O_DIRECTORY)

# Send request
s.send(req.SerializeToString())

# Recv response
resp		= rpc.criu_resp()
MAX_MSG_SIZE	= 1024
resp.ParseFromString(s.recv(MAX_MSG_SIZE))

if resp.type != rpc.DUMP:
	print 'Unexpected msg type'
	sys.exit(-1)
else:
	if resp.success:
		print 'Success'
	else:
		print 'Fail'
		sys.exit(-1)

	if resp.dump.restored:
		print 'Restored'
