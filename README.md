## Asynchronous HTTP proxy with tunnelling support

Built using Tornado (tested with version 2.2), supports HTTP GET, POST and
CONNECT methods.

Can be used as standalone script, or integrated with your Tornado app.


### Setup

    # run self tests
    python setup.py test

    # install it
    python setup.py install

### Command-line usage

    python tornado_proxy/proxy.py 8888


### Module usage

    from tornado_proxy import run_proxy
    run_proxy(port, start_ioloop=False)
    ...
    tornado.ioloop.IOLoop.instance().start()


### License and copyright

Copyright (C) 2012 Senko Rasic <senko.rasic@dobarkod.hr>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
