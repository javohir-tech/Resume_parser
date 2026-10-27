export const INPUT_LIMITS = {
    personal : {
        fullName : 150 ,
        professionalTitle : 750 , 
        email : 254 , 
        phone : 32 , 
        location : 150 , 
        website : 2048 , 
        github_link : 2048 , 
        linkedin_link : 2048 , 
        summary : 2000 
    } , 
    experience : {
        position : 150 , 
        company : 150 , 
        location : 150 , 
        description  : 2000
    } , 
    education : {
        degree : 150 , 
        fieldOfStudy : 150 , 
        institution : 150 , 
        location : 150 
    }, 
    language : {
        language : 150 , 
        degree : 150
    } , 
    skills_group : {
        title : 150
    } , 
    skill_item : {
        skill : 150
    }
} as const