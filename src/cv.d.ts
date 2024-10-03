export interface CV {
  basics: Basics;
  awards: Array<Awards>;
  projects: Array<Projects>;
}

interface Basics {
  name: string;
  label: string;
  image: string;
  email: string;
  url: string;
  summary: string;
  location: Location;
  profiles: Array<Profiles>;
}

interface Location {
  address: string;
  postalCode: string;
  city: string;
  countryCode: string;
  region: string;
}

interface Profiles {
  network: string;
  username: string;
  url: string;
}

type DateStr = `${string}-${string}-${string}`;

interface Awards {
  title: string;
  date: string;
  awarder: string;
  summary: string;
}

interface Projects {
  name: string;
  isActive: boolean;
  description: string;
  highlights: Highlight;
  url: string;
  github?: string;
}
type Highlight = Array<String>;
