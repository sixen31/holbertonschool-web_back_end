import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.allSettled([uploadPhoto(), createUser()])
    .then((results) => {
      const successes = results.filter(result => result.status == 'fulfilled');
      
      if (successes.length == 2) {
        const [picture, user] = successes.map(result => result.value);
        console.log(`${picture.body} ${user.firstName} ${user.lastName}`);
      } else {
        console.log('Signup system offline');
      }
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
