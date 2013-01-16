#!/usr/bin/env python

# Copyright (C) 2010-2012 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sample models for applying unapplied writes."""


from google.appengine.ext import db


class MyModel(db.Model):
  """A dummy model that may have had unapplied writes."""
  color = db.StringProperty()
  weight = db.IntegerProperty()


class __unapplied_write__MyModel(db.Expando):
  """An Expando model for reading entities which are in unapplied writes.

  We use an Expando model because any entity can be read into this, no matter
  what the underlying schema was.
  """
