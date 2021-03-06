"""
Name:        Redis Training Web App
Purpose:     Web front-end for Redis Training

Author:      Jeremy Nelson

Created:     2014/22/08
Copyright:   (c) Jeremy Nelson 2014
Licence:
"""
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = ''
__copyright__ = '(c) 2014 by Jeremy Nelson'

import os
import sys
from flask import Flask, render_template, abort
from collections import OrderedDict

TOPICS = OrderedDict([
    ('introducing-redis', {
        'location': '01-introducing-redis',
        'title': 'Introducing Redis'}),
    ('basic-setup-and-admin', {
        'location': '02-basic-setup-and-admin',
        'title': 'Basic Setup and Admin'}),
    ('redis-data-types', {
        'location': '03-redis-data-types',
        'title': 'Redis data types'}),
    ('operating-a-redis-system', {
        'location': '04-operating-a-redis-system',
        'title': 'Operating a Redis System'}),
    ('programming-redis', {
        'location': '05-programming-redis',
        'title': 'Programming Redis'}),
    ('pipelining-and-mass-insertions', {
        'location': '06-pipelining-and-mass-insertions',
        'title': 'Pipelining and Mass Insertions of Data'}),
    ('memory-expiration-and-key-eviction', {
        'location': '07-memory-expiration-and-key-eviction',
        'title': 'Memory, expiration and key eviction'}),
    ('transactions-and-locks', {
        'location': '08-transactions-and-locks',
        'title': 'Transactions and Locks'}),
    ('replication-and-pubsub', {
        'location': '09-replication-and-pubsub',
        'title': 'Replication and Pub/Sub'}),
    ('clustering-and-ha', {
        'location': '10-clustering-and-ha',
        'title': 'Clustering and High Availability'}),
    ('lua-scripting', {
        'location': '11-lua-scripting',
        'title': 'Lua Scripting'}),
    ('security', {
        'location': '12-security',
        'title': 'Security'})])

TOPIC_ORDER = list(TOPICS.keys())

app = Flask(__name__)

@app.route("/badge")
def badge():
    return render_template(
        'badge.html',
        section='badge',
        topics=TOPICS)

@app.route("/contact")
def contact():
    return render_template(
        'contact.html',
        section='contact',
        topics=TOPICS)

@app.route("/redis-virtual-machine")
@app.route("/redis-vm")
def redis_course_vm():
    return render_template(
        'redis-training-vm.html',
        section='topic',
        topics=TOPICS)

@app.route("/<topic>")
def topic_view(topic):
    if not topic in TOPICS:
        abort(404)
    position = TOPIC_ORDER.index(topic)
    next_topic, previous_topic = None, None
    if position+1 < len(TOPIC_ORDER):
        next_topic = {
            'key': TOPIC_ORDER[position+1],
            'title': TOPICS[TOPIC_ORDER[position+1]]['title']}
    if position-1 >= 0:
        previous_topic = {
            'key': TOPIC_ORDER[position-1],
            'title': TOPICS[TOPIC_ORDER[position-1]]['title']
            }
    return render_template(
        "{}.html".format(topic),
        section='topic',
        next=next_topic,
        previous=previous_topic,
        topics=TOPICS)

@app.route("/")
def home():
    return render_template("index.html",
        section='home',
        topics=TOPICS)

def main():
    host = '0.0.0.0'
    port = 8023
    app.run(
        debug=True,
        host=host,
        port=port
    )

if __name__ == '__main__':
    main()
