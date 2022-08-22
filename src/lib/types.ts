export type ProjectStatus = 'DONE' | 'WIP' | 'ARCHIVED' | 'ABANDONED';

export interface Button {
    name: string,
    link: string,
}

export interface Project {
    title: string,
    description: string,
    languages: string[],
    status: ProjectStatus,
    source?: string,
    forkedFrom?: string,
    image?: string,
    buttons?: Button[],
    tags?: string[],
}
