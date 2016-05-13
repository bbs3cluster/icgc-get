#
# Copyright (c) 2016 The Ontario Institute for Cancer Research. All rights reserved.
#
# This program and the accompanying materials are made available under the terms of the GNU Public License v3.0.
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from ..run_command import run_command, run_test_command
import tempfile


def genetorrent_call(uuid, token, tool_path, children, output):
    call_args = [tool_path, '-vv', '--max-children', children, '-c', token, '-d']
    call_args.extend(uuid)
    call_args.extend(['-p', output])
    code = run_command(call_args)
    return code


def genetorrent_manifest_call(manifest, token, tool_path, children, output):
    t = tempfile.NamedTemporaryFile()
    t.write(manifest)
    t.seek(0)
    call_args = [tool_path, '-vv', '--max-children', children, '-c', token, '-d', t.name, '-p', output]
    code = run_command(call_args)
    return code


def genetorrent_access_check(uuid, token, tool_path, output):
    call_args = [tool_path, '-vv', '-c', token, '-d']
    call_args.extend(uuid)
    call_args.extend(['-p', output])
    result = run_test_command(call_args)
    if result == 0:
        return True
    else:
        return False