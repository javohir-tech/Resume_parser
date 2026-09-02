interface Experience {
  id: string;
  position: string;
  company: string;
  location?: string;
  startDate: string;
  endDate?: string;
  description?: string;
}

interface Education {
  id: string;
  degree: string;
  institution: string;
  location?: string;
  startDate: string;
  endDate?: string;
}

interface SkillGroup {
  id: string;
  title: string;
  skills: string[];
}

interface Personal {
  fullname: string;
  title?: string;
  email?: string;
  phone?: string;
  location?: string;
  website?: string;
  summary?: string;
}

export interface Resume extends Personal {
  skills?: SkillGroup[];
  education?: Education[];
  experience?: Experience[];
}
