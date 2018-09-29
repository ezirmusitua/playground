import * as fs from 'fs';
import * as path from 'path';

export function listdir(target) {
  return fs.readdirSync(target)
           .map(d => ({
             name: d,
             path: path.join(target, d),
           }));
}

